//package rx
//
//import rx.lang.kotlin.subscribeBy
//import rx.schedulers.Schedulers
//import util.currentThreadName
//import java.util.*
//
//fun intenseCalculation(value: String): String {
//    println("starting thread with ${value}: ${currentThreadName()}")
//    val time: Long = (Random().nextInt(10) + 5) * 1000L
//    Thread.sleep(10000)
//    println("end thread with value: $value: ${currentThreadName()}")
//    return value
//}
//
//fun main(args: Array<String>) {
//    Observable.from(listOf("1","2","3","4","5", "6","7"))
////            .subscribeOn(Schedulers.computation())
//            .flatMap({
//                Observable.just (it)
//                        .subscribeOn(Schedulers.io())
//                        .map { intenseCalculation(it) }
//            })
//            .subscribeBy (onNext = { println(it) })
//    println("no blocked")
//    Thread.sleep(100000)
//}
//
//
//
