package demo

import kotlinx.coroutines.experimental.CommonPool
import kotlinx.coroutines.experimental.launch
import java.util.concurrent.atomic.AtomicInteger

fun main(args: Array<String>) {
    val c = AtomicInteger()

    for (i in 1..1_000_000)
        launch(CommonPool) {
            c.addAndGet(i)
        }

    println(c.get())
}