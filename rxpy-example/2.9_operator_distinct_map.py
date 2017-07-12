from __future__ import print_function
from rx import Observable, Observer

Observable.from_(["Alpha", "Beta", "Gamma", "Delta", "Epsilon"]) \
    .map(lambda s: len(s)) \
    .distinct() \
    .subscribe(lambda i: print(i))


Observable.from_(["Alpha", "Beta", "Gamma", "Delta", "Epsilon"]) \
    .distinct(lambda s: len(s)) \
    .subscribe(lambda i: print(i))