from __future__ import print_function
from rx import Observable


foo = Observable.interval(100).take(5)


foo.delay_with_selector(lambda x: Observable.interval(x * x * 1000).take(1)) \
    .subscribe(on_next = lambda x: print(x), on_completed=lambda: print("complete"))


input("ok\n")