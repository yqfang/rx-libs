//package rx
//
//import rx.lang.kotlin.subscribeBy
//import rx.schedulers.Schedulers
//import util.currentThreadName
//
//fun main(args: Array<String>) {
//    var observable: Observable<Int>?  = null
//
//    observable = Observable.just(42)
//    observable.subscribeBy(
//            onNext = {println(it)}
//    )
//    observable = Observable.from(listOf<Int>(1, 2, 3))
//    observable.subscribeBy(
//            onNext = {println("${it}, ${currentThreadName()}")}
//    )
//    observable.subscribeOn(Schedulers.newThread()).subscribeBy(
//            onNext = {println("${it}, ${currentThreadName()}")}
//    )
//
//}