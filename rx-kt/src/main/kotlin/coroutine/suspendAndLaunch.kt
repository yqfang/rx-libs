package coroutine

import kotlinx.coroutines.experimental.CommonPool
import kotlinx.coroutines.experimental.delay
import kotlinx.coroutines.experimental.launch
import kotlinx.coroutines.experimental.runBlocking
import util.currentThreadName
import kotlin.system.measureTimeMillis

fun main(args: Array<String>) = runBlocking<Unit> {
    println("launch from ${currentThreadName()}")

    launch(CommonPool) {
        val time = measureTimeMillis {
            val one = doSomethingUsefulOne()
            val two = doSomethingUsefulTwo()
            println("The answer is ${one + two}, ${currentThreadName()}")
        }
        println("Completed in $time ms")
    }
    Thread.sleep(100000)
}

suspend fun doSomethingUsefulOne(): Int {
    println("one: ${currentThreadName()}")
    delay(2000L) // pretend we are doing something useful here
    return 13
}

suspend fun doSomethingUsefulTwo(): Int {
    println("two: ${currentThreadName()}")

    delay(2000L) // pretend we are doing something useful here, too
    return 29
}