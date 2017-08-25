package rx2

import io.reactivex.Observable
import io.reactivex.rxkotlin.subscribeBy
import java.lang.Thread.sleep
import java.util.concurrent.TimeUnit

fun main(args: Array<String>) {
    val secondIntervals: Observable<Long> =
            Observable.interval(1, TimeUnit.SECONDS)
    secondIntervals.subscribeBy { println(it) }

    sleep(50000)

}