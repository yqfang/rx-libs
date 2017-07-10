from __future__ import print_function
from rx import Observable, Observer

source = Observable.from_(["hello","world"])


source.subscribe(on_next=lambda s: print("Receive {0}".format(s)), on_completed=lambda: print('Done'))


