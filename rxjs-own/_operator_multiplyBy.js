/**
 * Created by yqfang on 2017/7/15.
 */

const { Observable } = require('rxjs/Rx');
const { Subject } = require('rxjs/Rx');


var foo = Observable.interval(1000)

function multipleBy(multiplier) {
    var source = this

    var result = Observable.create(function subscribe(observer) {
        source.subscribe(
            function (x) {observer.next(x * multiplier)},
            function (err) {observer.error(err)},
            function () {observer.complete()}
        )
    })
    return result
}

Observable.prototype.multipleBy = multipleBy


foo.multipleBy(2).take(3).subscribe((i) => console.log(i))