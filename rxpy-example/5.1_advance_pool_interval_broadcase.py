from __future__ import print_function

from rx import Observable, Observer
from rx.concurrency import ThreadPoolScheduler
from threading import current_thread
import multiprocessing, time, random

optimal_thread_count = multiprocessing.cpu_count() + 1
pool_scheduler = ThreadPoolScheduler(optimal_thread_count)


#         .switch_map(lambda i: Observable.from_(running_tasks).subscribe_on(pool_scheduler).map(lambda s: print_task_st(s))) \

a = Observable.interval(1000).switch_map(lambda i: Observable.just(i).subscribe_on(pool_scheduler)).publish().ref_count()

a.subscribe(lambda i: print("first observer {0}, {1}".format(i, current_thread().name)))
time.sleep(5)
a.subscribe(lambda i: print("second observer {0}, {1}".format(i, current_thread().name)))

while True:
    pass