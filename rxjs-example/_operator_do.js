/**
 * Created by yqfang on 2017/7/16.
 */

var Rx = require('rxjs/Rx');

Rx.Observable.of(1,2,3)

var foo = Rx.Observable.interval(200).take(4);

// do is just a special case of map, is really useful for debugging
var bar = foo.do(function(x) {
    console.log("!" + x)
})


bar.subscribe(() => {})