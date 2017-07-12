/**
 * Created by yqfang on 2017/7/10.
 */
var Rx = require('rxjs/Rx');


// Rx.Observable.interval(100).map((i) => String.fromCharCode(i + 65)).take(5)
//     .subscribe((s) => console.log(s))


Rx.Observable.interval(100).map((i) => Array.from("7ujm&UJM")[i]).take(8)
    .subscribe((s) => console.log(s))