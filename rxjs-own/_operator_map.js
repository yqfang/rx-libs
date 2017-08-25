const { Observable } = require('rxjs/Rx');



function mmap(tranformFn) {
    var source = this

    return Observable.create(function subscribe(observer) {
        source.subscribe(
            function(x) {
                observer.next(tranformFn(x))
            },
            function(err) {
                observer.error(err)
            },
            function() {
                observer.complete()
            }
        )
    })
}

function miterval(millsecond) {
    return Observable.create(function subscribe(observer) {
        var n = 0
        var cancel = setInterval(function() {
            observer.next(n)
            n += 1
        }, millsecond)
    })
}

function mtake(num) {
    var source = this;

    return Observable.create(function subscribe(observer) {
        source.subscribe(
            function(x) {
                if(!num) {
                    observer.complete()
                }
                observer.next(x)
                num --
            },
            function(err) {
                observer.error(err)
            },
            function() {
                observer.complete()
            }
        )
    })
}

Observable.miterval = miterval
Observable.prototype.mmap = mmap
Observable.prototype.mtake = mtake

source = Observable.miterval(1000)

source.mtake(2).subscribe((x) => console.log(x),(err) => console.err(err), () => console.log("DONE!"))

