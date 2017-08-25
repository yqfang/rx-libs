from __future__ import print_function
from rx import Observable



foo = Observable.interval(100).take(5)

foo.debounce(1000).subscribe(lambda s: print(s), on_completed=lambda : print("DONE"))



input("ok\n")