from __future__ import print_function
from rx import Observable, Observer

Observable.from_([4,76,22,66,881,13,35]) \
    .reduce(lambda x, y: x + y) \
    .subscribe(lambda i: print(i))