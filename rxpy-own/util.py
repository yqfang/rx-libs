import multiprocessing, time, random
import subprocess
from rx import Observable, Observer
from rx.concurrency import ThreadPoolScheduler
def singleton(cls, *args, **kw):
    instances = {}
    def _singleton():
        if cls not in instances:
            instances[cls] = cls(*args, **kw)
        return instances[cls]
    return _singleton

# calculate number of CPU's and add 1, then create a ThreadPoolScheduler with that number of threads
optimal_thread_count = multiprocessing.cpu_count() + 1
pool_scheduler = ThreadPoolScheduler(optimal_thread_count)


def getIntervalOb(time):
    return Observable.interval(time).switch_map(lambda i: Observable.just(i).subscribe_on(pool_scheduler))