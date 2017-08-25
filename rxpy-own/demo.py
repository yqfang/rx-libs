from __future__ import print_function

from rx import Observable, Observer

from threading import current_thread
from util import *

import os
import signal
import time
import json


@singleton
class ObservableWrapper():
    def __init__(self):
        self.task_producer = None
        self.running_tasks = []
        self.feedback_tasks = {}
    # mock the pub
    def publish_tasks(self,file_name):
        def task_from_file(file_name):
            try:
                with open(file_name) as data_file:
                    script = json.load(data_file)
                    # parse, clean, and push words in text file
                    return Observable.from_(script).distinct(lambda t: t['timestamp'])
            except Exception, Argument:
                print(Argument)
                return Observable.empty()
        if self.task_producer is None:
            self.task_producer = getIntervalOb(1000).flat_map(lambda i: task_from_file(file_name)).distinct().publish().ref_count()

        return self.task_producer


def create_tasks_ob(script_name):
    return ObservableWrapper().publish_tasks(script_name)

# create_tasks_ob("script2.json").subscribe(lambda t: print (t))

def fileOb(file_name):
    file = open(file_name, 'r')
    return Observable.from_(file)

def add_task(task):
    p = subprocess.Popen('exec /Users/yqfang/.pyenv/versions/2.6.9/bin/python 10s_process.py > {0}_log.txt'.format(task['name']), shell=True)
    ObservableWrapper().running_tasks.append((task, p))
    print("add {0}(timestamp:{3}), pid: {1}, current thread {2} from thread pool".format(task['name'], p.pid, current_thread().name, task['timestamp']))
    return (task, p)

def get_task_info(task):
    for t in ObservableWrapper().running_tasks:
        if task['name'] == t[0]['name']:
            return t
# def remove_task(task):
#     for t in ObservableWrapper().running_tasks:
#         if task['name'] == t[0]['name']:
#             ObservableWrapper().running_tasks.remove(t)
def kill_task(task):
    pid = get_task_info(task)[1].pid
    get_task_info(task)[1].kill()
    time.sleep(3)
    print("kill {0}(timestamp:{3}), stat is: {1}, current thread {2} from thread pool".format(task['name'], "ok" if str(get_task_info(task)[1].poll()) == 'None' else get_task_info(task)[1].poll(), current_thread().name, task['timestamp']))
    return get_task_info(task)
    # remove_task(task)
def stat_task(task):
    info = get_task_info(task)
    st = info[1].poll()
    print("the  {0}(timestamp:{3}), stat is : {1}, current thread {2} from thread pool".format(task['name'], "ok" if str(st) == 'None' else st , current_thread().name, task['timestamp']))
    return info

def do_task_by_type(task):
    if "add" == task['type']:
        ret = add_task(task)
        ObservableWrapper().feedback_tasks[task['timestamp']] = {'pid': ret[1].pid, 'status': "ok" if str(ret[1].poll()) == 'None' else ret[1].poll()}
    elif "kill" == task['type']:
        ret = kill_task(task)
        ObservableWrapper().feedback_tasks[task['timestamp']] = {'pid': ret[1].pid, 'status': "ok" if str(ret[1].poll()) == 'None' else ret[1].poll()}
    elif "stat" == task['type']:
        ret = stat_task(task)
        ObservableWrapper().feedback_tasks[task['timestamp']] = {'pid': ret[1].pid, 'status': "ok" if str(ret[1].poll()) == 'None' else ret[1].poll()}
    elif "log" == task['type']:
        ObservableWrapper().feedback_tasks[task['timestamp']] = []
        getIntervalOb(1000).flat_map(lambda i: i, fileOb("{0}_log.txt".format(task['name']))).distinct() \
            .subscribe(lambda i: ObservableWrapper().feedback_tasks[task['timestamp']].append(i))
    else:
        pass

task_ob = create_tasks_ob("script.json").subscribe(lambda task: do_task_by_type(task))

getIntervalOb(1000).flat_map(lambda i: Observable.from_(ObservableWrapper().feedback_tasks.keys())).distinct().subscribe(lambda s: print("feedback queue add feedback {0}".format({s: ObservableWrapper().feedback_tasks[s]})))

input("\n")