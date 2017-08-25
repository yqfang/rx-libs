package rx2

import io.reactivex.Observable
import io.reactivex.rxkotlin.subscribeBy

fun main(args: Array<String>) {
    val start: Int = 1
    var count: Int = 5

    val source: Observable<Int> = Observable.defer { Observable.range(start, count) }

    source.subscribeBy { println("Observer1: $it") }
    count = 10
    source.subscribeBy { println("Observer2: $it") }
}