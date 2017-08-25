from __future__ import print_function
from rx import Observable

foo = Observable.interval(500).take(5) \
            .zip(Observable.from_('hello'), lambda x, y: y)

bar = Observable.interval(300).take(7) \
    .zip(Observable.of(0, 1, 0, 1, 0, 1, 0), lambda x, y: y)


            # -----H-----e-----l-----l-----o
            #---0---1---0---1---0---1---0
            #------h-----e-----L-----l-----o

            # .subscribe(lambda x: print(x), lambda err: print(x), lambda : print("complete"))

foo.with_latest_from(bar, lambda x, y: x.upper() if y == 1 else x.lower()) \
        .subscribe(lambda x: print(x), lambda err: print(err), lambda : print("complete"))

input("Press some keys\n")


#
# Let's try using it in practice here, and we hit that function to combine the values. Let's run this, and we see there a lower case "H," lower case "E-L-L-O," just like we had outlined here. We use withLatestFrom to map an observable, foo, to another observable, but using the latest value from some other observables.
# That is why there is no static version of the withLatestFrom operator. That's because foo here is somehow special. It's different. It's assuming a different responsibility than bar is because essentially it's not like CombineLatest. If we would use CombineLatest, then when one is emitted on bar, it would be combined with latest value from "H" and that would make upper case "H," but that's not what we want.
# We want basically this to be a mapping of that observable, just using some secondary information from other observables. The main observable is foo, that's what we want to map. That's why foo here is special because it's the main observable and we just want to use secondary information from other observables.