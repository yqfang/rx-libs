from __future__ import print_function
from rx import Observable, Observer


Observable.from_([4,76,22,66,881,13,35]) \
    .scan(lambda total, value: total + value) \
    .subscribe(lambda s: print(s))


# Scan is really useful because, in a sense, it accumulates state. The accumulator is a state. It basically is a memory here. Basically, when we see E, there is state stored inside the scan operator, which is the accumulator, and then this is how things work over time.
# One of the useful applications for scan is, let's say when you have an observable here, I'm just going to draw it. These are click events happening on some button. Then you can map each of these click events to the number one, and then you get here, one, one, and one.
# Then, if you use scan, here now let's give the seed as zero. It means that once it sees one, it will add zero plus one to give us one here. Then once it sees one here, it will add that to the accumulator, which was one, and we will get two. Now the accumulator is two, and once it sees one again, it's going to add two plus one to give us three.
# Basically, if this first observable here was an observable of clicks, now this is the number of times that that button was clicked. There you can see how scan accumulates a state, and is really useful in these cases.
# Scan is a horizontal combination operator, which means that the values that it's combining are coming from just one observable.