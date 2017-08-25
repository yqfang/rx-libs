package rx2

import io.reactivex.Observable
import io.reactivex.observables.ConnectableObservable
import io.reactivex.rxkotlin.subscribeBy

fun main(args: Array<String>) {
    val source: ConnectableObservable<String> =
            Observable.just("Alpha", "Beta", "Gamma", "Delta", "Epsilon").publish()

    source.subscribeBy { println("Observer1: $it") }
    source.map { it.length }.subscribeBy { println("Observer1: $it") }

    source.connect()
}