from __future__ import print_function
from rx import Observable
list = ["Alpha","Beta","Gamma","Delta","Epsilon"]
letters = Observable.from_(list)
intervals = Observable.interval(1000)

Observable.zip(letters,intervals, lambda s,i: s) \
    .subscribe(lambda s: print(s))
# intervals = Observable.interval(1000).take(len(list))
# intervals \
#     .map(lambda i: list[i]) \
#     .subscribe(lambda s: print(s))

input("Press any key to quit\n")