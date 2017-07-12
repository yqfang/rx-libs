from __future__ import print_function
from rx import Observable
from threading import current_thread
import time, random

def intense_calculation(value):
    # sleep for a random short duration between 0.5 to 2.0 seconds to simulate a long-running calculation
    time.sleep(random.randint(5,20) * .1)
    return value

# Create Process 1
Observable.from_(["Alpha","Beta","Gamma","Delta","Epsilon"]) \
    .map(lambda s: intense_calculation(s)) \
    .subscribe(on_next=lambda s: print("PROCESS 1: {0} {1}".format(current_thread().name, s)),
               on_error=lambda e: print(e),
               on_completed=lambda: print("PROCESS 1 done!"))

# Create Process 2
Observable.range(1,10) \
    .map(lambda s: intense_calculation(s)) \
    .subscribe(on_next=lambda i: print("PROCESS 2: {0} {1}".format(current_thread().name, i)),
               on_error=lambda e: print(e),
               on_completed=lambda: print("PROCESS 2 done!"))

input("Press any key to exit\n")