from __future__ import print_function
from rx import Observable, Observer


Observable.from_(["Alpha","Beta","Gamma","Delta","Epsilon"]) \
    .to_list() \
    .subscribe(lambda s: print(s))