from __future__ import print_function
from rx import Observable, Observer

Observable.from_(['1', '2', '3', '10', '100', '5']) \
    .map(lambda s: int(s)) \
    .take_while(lambda i: i < 10) \
    .subscribe(on_next = lambda i: print(i), on_completed = lambda: print("Done"))