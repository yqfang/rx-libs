//package rx
//
//import rx.lang.kotlin.subscribeBy
//import rx.schedulers.Schedulers
//
//fun main(args: Array<String>) {
//    Observable.from(listOf("1","2","3","4","5", "6","7","1","2","3","4","5", "6","7"))
//            .flatMap({
//                Observable.just (it)
//                        .subscribeOn(Schedulers.io())
//                        .map { intenseCalculation(it) }
//            }, 2).toList()
//            .subscribeBy (onNext = { println(it) })
//    println("no blocked")
//    Thread.sleep(100000)
//}