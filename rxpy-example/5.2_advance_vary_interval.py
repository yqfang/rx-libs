from __future__ import print_function

from rx import Observable, Observer
from rx.concurrency import ThreadPoolScheduler
from threading import current_thread
import multiprocessing, time, random


optimal_thread_count = multiprocessing.cpu_count() + 1
pool_scheduler = ThreadPoolScheduler(optimal_thread_count)


def timed_tasks_ob(time_arr, task_arr):
    return Observable.from_(time_arr).flat_map(lambda i: Observable.timer(i * 1000).switch_map(lambda i: Observable.just(i).subscribe_on(pool_scheduler))).zip(Observable.from_(task_arr), lambda x, y: y).publish().ref_count()

ob = timed_tasks_ob([1, 2, 3, 4], ["a", "b", "c", "d"])
ob.subscribe(lambda i: print("1, {0},{1}".format(i, current_thread().name)))
time.sleep(2)
ob.subscribe(lambda i: print("2, {0},{1}".format(i, current_thread().name)))

input("")