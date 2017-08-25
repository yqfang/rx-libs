package demo

import java.util.concurrent.atomic.AtomicInteger
import kotlin.concurrent.thread

fun main(args: Array<String>) {
    val c = AtomicInteger()

    for (i in 1..1_000_000)
        thread(start = true) {
            c.addAndGet(i)
        }

    println(c.get())
}
