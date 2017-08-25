from __future__ import print_function

from rx import Observable, Observer
from rx.concurrency import ThreadPoolScheduler
from threading import current_thread
import multiprocessing, time, random
import subprocess
import os
import signal
import time
import json

# calculate number of CPU's and add 1, then create a ThreadPoolScheduler with that number of threads
optimal_thread_count = multiprocessing.cpu_count() + 1
pool_scheduler = ThreadPoolScheduler(optimal_thread_count)

def singleton(cls, *args, **kw):
    instances = {}
    def _singleton():
        if cls not in instances:
            instances[cls] = cls(*args, **kw)
        return instances[cls]
    return _singleton

# class create_task_Observer(Observer):
#     def on_next(self, value):
#         ready_tasks.append("task_{0}".format(value))
#         print("From server task_{0} is added to ready-task queue".format(value))
#     def on_completed(self):
#         pass
#     def on_error(self, error):
#         pass


@singleton
class ObservableWrapper():
    def __init__(self):
        self.task_producer = None
        self.running_tasks = []
    # mock the pub
    def publish_tasks(self, time_arr, task_arr):
        if self.task_producer is None:
            self.task_producer =  Observable.from_(time_arr).flat_map(lambda i: Observable.timer(i * 1000).switch_map(lambda i: Observable.just(i).subscribe_on(pool_scheduler))).zip(Observable.from_(task_arr), lambda x, y: y).publish().ref_count()
        return self.task_producer

def create_tasks_ob(script_name):
    with open(script_name) as data_file:
        script = json.load(data_file)
        def get_timer(script):
            time_arr = []
            Observable.from_(script).map(lambda e: e['sequence']).subscribe(lambda s: time_arr.append(s))
            return time_arr
        return ObservableWrapper().publish_tasks(get_timer(script), script)



def add_task(task):
    p = subprocess.Popen('exec /Users/yqfang/.pyenv/versions/2.6.9/bin/python 10s_process.py > {0}_log.txt'.format(task['name']), shell=True)
    ObservableWrapper().running_tasks.append((task, p))
    print("add {0}, pid: {1}, current thread{2}".format(task['name'], p.pid, current_thread().name))
    return p.pid

def get_task_info(task):
    for t in ObservableWrapper().running_tasks:
        if task['name'] == t[0]['name']:
            return t
def remove_task(task):
    for t in ObservableWrapper().running_tasks:
        if task['name'] == t[0]['name']:
            ObservableWrapper().running_tasks.remove(t)
def kill_task(task):
    pid = get_task_info(task)[1].pid
    get_task_info(task)[1].kill()
    print("kill {0}, sts: {1}, cur thread, {2}".format(task['name'], get_task_info(task)[1].pid, current_thread().name))
    # remove_task(task)
def stat_task(task):
    st = get_task_info(task)[1].poll()
    print("the  {0}, stat is : {1}, current thread {2}".format(task['name'], st, current_thread().name))
    if str(st) == 'None':
        return "ok"
    else:
        return st

def do_task_by_type(task):
    if "add" == task['type']:
        return add_task(task)
    elif "kill" == task['type']:
        return kill_task(task)
    elif "stat" == task['type']:
        return stat_task(task)
    else:
        pass

class TaskObserver(Observer):
    def on_next(self, task):
        do_task_by_type(task)
    def on_completed(self):
        pass
    def on_error(self, error):
        pass

task_ob = create_tasks_ob("script.json").subscribe(TaskObserver())





input("\n")


# ob = ObservableWrapper()
#
# a.publish_tasks(15)
#
# input("")
#
#
# def do_task(task_info):
#     p = subprocess.Popen("/Users/yqfang/.pyenv/versions/2.6.9/bin/python 10s_process.py > output_{0}.txt".format(task_info), shell= True)
#     running_tasks.append((task_info, p))
#     ready_tasks.remove(task_info)
#     return (task_info, p)
#




# def dispach_task():
#     Observable.interval(6000) \
#         .switch_map(lambda i: Observable.from_(ready_tasks).subscribe_on(pool_scheduler).map(lambda r: do_task(r))) \
#         .subscribe(on_next=lambda i: print("start task: {0} with thread {1}".format(i, current_thread().name)), on_error=lambda e: print(e))
#
# def print_task_st(t):
#     return "task_name: {0} is running and the task_st: {1}".format(t[0], "ok" if t[1].poll() is None else t[1].poll())
#
# def watch_running_task():
#     Observable.interval(7000) \
#         .switch_map(lambda i: Observable.from_(running_tasks).subscribe_on(pool_scheduler).map(lambda s: print_task_st(s))) \
#         .subscribe(on_next=lambda s: print("Received {0} on {1}, running-size: {2}, ready_running-size: {3}".format(s, current_thread().name, len(running_tasks), len(ready_tasks))))
#
#
# create_task(5)
# dispach_task()
# watch_running_task()
#
# while True:
#     time.sleep(5)

# Observable.interval(2000) \
#     .map(lambda i: Observable.from_(sp).map(lambda p: (i, p.poll()))) \
#     .merge_all() \
#     .subscribe(lambda s: print(s))