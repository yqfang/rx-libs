package demo

import kotlinx.coroutines.experimental.CommonPool
import kotlinx.coroutines.experimental.async
import kotlinx.coroutines.experimental.runBlocking

fun main(args: Array<String>) {
    val deferred = (1..1_000_000).map {
        n -> async(CommonPool) {
            n
        }
    }
    runBlocking {
        val sum = deferred.sumBy { it.await() }
        println("Sum: $sum")
    }
}