from __future__ import print_function
from rx import Observable, Observer


foo = Observable.of('h', 'e', 'l', 'l', 'o') \
        .zip(Observable.interval(600).take(5), lambda x, y: x)

# -----h-----e-----l-----l-----o|
#
# buffer_with_count(2)
#
# ----------[h,e]-------[l,l]--[o]|


# -----h-----e-----l-----l-----o|
# --------x--------x--------x
# buffer_with_time(9000)
#
# --------h--------e--------ll-0|


# -----h-----e-----l-----l-----o| (foo)
# buffer(closing observable)
# --------0--------1--------2|    (bar)
#
# -------h-------e---------ll|

bar = Observable.interval(800).take(3)

# foo.buffer_with_count(2).subscribe(lambda x: print(x))
# foo.buffer_with_time(900).subscribe(lambda x: print(x))
foo.buffer(bar).subscribe(lambda x: print(x), lambda err: print(err), lambda : print("DONE"))


input("Press some key to quit\n")