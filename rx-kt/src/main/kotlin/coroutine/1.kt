package coroutine

import kotlinx.coroutines.experimental.CommonPool
import kotlinx.coroutines.experimental.delay
import kotlinx.coroutines.experimental.launch
import kotlinx.coroutines.experimental.runBlocking
import util.currentThreadName
import kotlin.concurrent.thread
import kotlin.coroutines.experimental.buildSequence

val fibonacciSeq = buildSequence {
    var a = 0
    var b = 1

    yield(1)

    while (true) {
        yield(a + b)

        val tmp = a + b
        a = b
        b = tmp
    }
}

fun main(args: Array<String>) {
    val res = fibonacciSeq
            .take(5)
            .toList()
    println(res)
}