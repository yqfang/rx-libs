//package rx
//
//import rx.lang.kotlin.toObservable
//import rx.schedulers.Schedulers
//import util.currentThreadName
//
//fun main(args: Array<String>) {
//    val list: List<Int> = listOf(1, 2, 3, 4)
//    println("driving thread: ${currentThreadName()}")
//    list.toObservable().subscribeOn(Schedulers.newThread())
//            .forEach() {
//        println("enter thread: ${currentThreadName()}")
//                Thread.sleep(3000)
//        println("value: $it")
//        println("exit thread: ${currentThreadName()}")
//    }
//    while(true){}
//}