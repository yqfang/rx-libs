from __future__ import print_function
from rx import Observable

source1 = Observable.from_(["Alpha","Beta","Gamma","Delta","Epsilon"])
source2 = Observable.from_(["Zeta","Eta","Theta","Iota"])

list = [source1, source2]


Observable.from_(list) \
    .concat_all() \
    .subscribe(lambda s: print(s))