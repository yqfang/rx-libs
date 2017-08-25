package rx2

import io.reactivex.Observable
import io.reactivex.rxkotlin.subscribeBy

fun main(args: Array<String>) {
    val source: Observable<String> = Observable.create{
        try {
            it.onNext("Alpha")
            it.onNext("Beta")
            it.onNext("Gamma")
            it.onNext("Delta")
            it.onNext("Epsilon")
            it.onComplete()
        } catch (e: Throwable) {
            it.onError(e)
        }
    }
    source.filter{it.length > 5}.subscribeBy(onNext={ println("RECEIVED: $it")}, onError = {it.printStackTrace()}, onComplete = {println("DONE")})
}