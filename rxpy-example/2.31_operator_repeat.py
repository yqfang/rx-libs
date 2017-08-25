from __future__ import print_function
from rx import Observable

Observable.just(43).do_while(lambda n: n.scan(lambda acc, x, i: acc + i, 0).delay(200).take_while(lambda count: count < 1)) \
    .subscribe(lambda i: print(i))