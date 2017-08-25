package rx2

import io.reactivex.Observable
import io.reactivex.rxkotlin.subscribeBy

fun main(args: Array<String>) {
    val myString: Observable<String>
            = Observable.just("Alpha", "Beta", "Gamma", "Delta", "Epsilon")

    myString.map{it.length}
        .subscribeBy(onNext = {println(it)})

}