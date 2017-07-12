from __future__ import print_function
from rx import Observable
import re

def words_from_file(file_name):
    file = open(file_name)
    return Observable.from_(file) \
        .flat_map(lambda l: Observable.from_(l.split())) \
        .map(lambda w: re.sub(r'[^\w]','', w)) \
        .filter(lambda w: w != "") \
        .map(lambda w: w.lower()) \


words_from_file("blog.txt") \
    .subscribe(lambda w: print (w))