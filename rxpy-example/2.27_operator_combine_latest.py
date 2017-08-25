from __future__ import print_function
from rx import Observable

# Just keep in mind that CombineLatest is an "and" style operator, and it's mainly useful when you have two independent sources of data such as foo and bar are considered to be very independent and of different nature, and you want to make a value, which takes values from both of these observables.
# One canonical example would be if you would be calculating your body mass index, that requires your weight and your height. If you consider that this weight and height would be observables, then we combine them together with a formula to calculate your body mass index. It's obvious why you can't use merge here because merge is an or style, and body mass index is not your weight or your height. It's both of them together, calculated as some formula.
# Here, we would put the formula for BMI. In general, that's what you should take out from this lesson is that merge is an "or" style combinator and CombineLatest is the "and" style.



foo = Observable.interval(500).take(4)
bar = Observable.interval(400).take(5)

# -----0-----1-----2-----3
# ----0----1----2----3----4
# -----0---1-2--3--4-5---67

# as an static operator
# Observable.combine_latest(foo, bar, lambda x, y: x + y) \
#     .subscribe(lambda x: print(x), lambda err: print(err), lambda : print("complete"))

# as an instance style


# merge: OR
# combineLatest: AND
foo.combine_latest(bar, lambda x, y: x + y) \
    .subscribe(lambda x: print(x), lambda err: print(err), lambda : print("complete"))

input("Press some key to quit\n")