from __future__ import print_function
from rx import Observable, Observer
import time

# Hot vs Cold Observables (https://medium.com/@benlesh/hot-vs-cold-observables-f8094ed53339)
# The source is cold because once a observer subscribe the source, the subscribe function will be invoked(in this example the from_([''...]) behind the scene)


source = Observable.from_(["Alpha","Beta","Gamma","Delta","Epsilon"])

source.subscribe(lambda s: print("Subscriber 1: {0}".format(s)))
time.sleep(5)
source.subscribe(lambda s: print("Subscriber 2: {0}".format(s)))