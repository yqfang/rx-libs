from __future__ import print_function
from rx import Observable, Observer


from rx import Observable
from threading import current_thread
import multiprocessing, time, random

Observable.interval(1000) \
    .map(lambda i: "{0} Mississippi from {1}".format(i, current_thread().name)) \
    .subscribe(lambda s: print(s))

input("Press any key to quit\n")