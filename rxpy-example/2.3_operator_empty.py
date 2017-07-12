from __future__ import print_function
from rx import Observable, Observer


Observable.empty() \
    .subscribe(on_next= lambda s: print(s),
               on_completed= lambda: print("Done!"))