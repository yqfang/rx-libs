from __future__ import print_function
from rx import Observable, Observer

Observable.from_(["Alpha","Beta","Gamma","Delta","Epsilon"]) \
    .map(lambda s: len(s)) \
    .filter(lambda s: len(s) >= 5) \
    .subscribe(lambda value: print(value))