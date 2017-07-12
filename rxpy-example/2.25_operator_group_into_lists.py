from __future__ import print_function
from rx import Observable

items = ["Alpha", "Beta", "Gamma", "Delta", "Epsilon"]

Observable.from_(items) \
    .group_by(lambda s: len(s)) \
    .map(lambda grp: grp.to_list()) \
    .merge_all() \
    .subscribe(lambda s: print(s))

