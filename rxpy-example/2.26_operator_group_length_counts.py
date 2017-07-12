from __future__ import print_function
from rx import Observable

items = ["Alpha", "Beta", "Gamma", "Delta", "Epsilon"]

Observable.from_(items) \
    .group_by(lambda s: len(s)) \
    .flat_map(lambda grp: grp.count().map(lambda cnt: (grp.key, cnt))) \
    .to_dict(lambda key_value: key_value[0], lambda key_value: key_value[1])\
    .subscribe(lambda d: print(d))