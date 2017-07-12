from __future__ import print_function
from rx import Observable, Observer

# Using Observable.range()
# create an Observable that emits a particular range of sequential integers
# http://reactivex.io/documentation/operators/range.html
letters = Observable.range(1, 10)
letters.subscribe(lambda value: print(value))


# Using Observable.just()
# create an Observable that emits a particular item
# http://reactivex.io/documentation/operators/just.html

greeting = Observable.just("Hello World!")
greeting.subscribe(lambda value: print(value))


books = Observable.of('ABC', 'EFG', 'HIJ') \
    .subscribe(lambda s: print(s))
