package rx2

import io.reactivex.Observable
import io.reactivex.rxkotlin.subscribeBy

fun main(args: Array<String>) {

    Observable.fromCallable { 1/0 }
            .subscribeBy(onNext = {println(it)}, onError = {println("error: $it")})
}