/**
 * Created by yqfang on 2017/7/16.
 */
var Rx = require('rxjs/Rx');

var foo = Rx.Observable.interval(500).take(4)
var bar = Rx.Observable.interval(300).take(5)

var combined = Rx.Observable.combineLatest(foo, bar, (x, y) => (x + y))


combined.subscribe((x) => console.log(x), (err) => console.err(err), () => console.log("complete"))