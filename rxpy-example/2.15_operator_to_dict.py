from __future__ import print_function
from rx import Observable, Observer

Observable.from_(["Alpha", "Beta", "Gamma", "Delta", "Epsilon"]) \
    .to_dict(lambda s: s[0]) \
    .subscribe(lambda i: print(i))

Observable.from_(["Alpha", "Beta", "Gamma", "Delta", "Epsilon"]) \
    .to_dict(lambda s: s[0], lambda s: len(s)) \
    .subscribe(lambda i: print(i))
