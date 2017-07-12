from __future__ import print_function
from rx import Observable, Observer
import time


from rx import Observable

disposable = Observable.interval(1000) \
    .map(lambda i: "{0} Mississippi".format(i)) \
    .subscribe(lambda s: print(s))

# sleep 5 seconds so Observable can fire(push to observer)

time.sleep(5)


print("Unsubscribing!")
disposable.dispose()

# sleep a bit longer to prove no more emissions are coming

time.sleep(5)