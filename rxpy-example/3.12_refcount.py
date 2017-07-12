from __future__ import print_function
from rx import Observable
import time

source = Observable.interval(1000).publish().ref_count()

source.subscribe(lambda s: print("Subscriber 1: {0}".format(s)))

# sleep 5 seconds, then add another subscriber
time.sleep(5)
un_subscribe = source.subscribe(lambda s: print("Subscriber 2: {0}".format(s)))

time.sleep(5)

un_subscribe.dispose()

time.sleep(5)

source.subscribe(lambda s: print("Subscriber 2: {0}".format(s)))
input("Press any key to exit\n")