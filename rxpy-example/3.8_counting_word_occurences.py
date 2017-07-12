from __future__ import print_function
from rx import Observable
import re

def words_from_file(file_name):
    file = open(file_name)
    return Observable.from_(file) \
        .flat_map(lambda l: Observable.from_(l.split())) \
        .map(lambda w: re.sub(r'[^\w]','', w)) \
        .filter(lambda w: w != "") \
        .map(lambda w: w.lower())

def count_occurences(file_name):
    words_from_file(file_name) \
        .group_by(lambda w : w) \
        .flat_map(lambda grp: grp.count().map(lambda cnt: (grp.key ,cnt))) \
        .to_dict(lambda t: t[0], lambda t: t[1]) \
        .subscribe(lambda l: print(l))


count_occurences("blog.txt")