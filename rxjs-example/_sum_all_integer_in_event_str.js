/**
 * Created by yqfang on 2017/7/10.
 */
var Rx = require('rxjs/Rx');

var result = Rx.Observable.interval(0).map((i) => ['1', '2', '3', 'hello', 'world'][i]).take(5)
    .map((s) => parseInt(s))
    .filter((i) => !isNaN(i))
    .reduce((x, y) => x + y);

result.subscribe((sum) => console.log(sum))