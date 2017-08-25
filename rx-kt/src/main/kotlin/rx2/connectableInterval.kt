package rx2

import io.reactivex.Observable
import io.reactivex.observables.ConnectableObservable
import io.reactivex.rxkotlin.subscribeBy
import java.lang.Thread.sleep
import java.util.concurrent.TimeUnit

fun main(args: Array<String>) {
    val seconds: ConnectableObservable<Long> =
            Observable.interval(1, TimeUnit.SECONDS).publish()

    seconds.subscribeBy { println("observer1: $it") }
    seconds.connect()
    sleep(5000)
    seconds.subscribeBy { println("observer2: $it") }

    sleep(100000)
}