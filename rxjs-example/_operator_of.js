var Rx = require('rxjs/Rx');

Rx.Observable.of(1,2,3)
    .map((x) => x * 2)
    .subscribe((x) => console.log(x))


