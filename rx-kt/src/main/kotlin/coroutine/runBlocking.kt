package coroutine

import kotlinx.coroutines.experimental.CommonPool
import kotlinx.coroutines.experimental.delay
import kotlinx.coroutines.experimental.launch
import kotlinx.coroutines.experimental.runBlocking
import util.currentThreadName

fun main(args: Array<String>) {
// What if there are no dependencies between invocation of doSomethingUsefulOne and doSomethingUsefulTwo
// and we want to get the answer faster, by doing both concurrently? This is where async comes to help.
// Conceptually, async is just like launch. It starts a separate coroutine which is a light-weight thread
// that works concurrently with all the other coroutines. The difference is that launch returns a Job and
// does not carry any resulting value, while async returns a Deferred -- a light-weight non-blocking future that
// represents a promise to provide a result later. You can use .await() on a deferred value to get its eventual result
// , but Deferred is also a Job, so you can cancel it if needed.

    println("Start")
    // Start a coroutine
    launch(CommonPool) {
        delay(1000)
        println("Hello ${currentThreadName()}")
    }
    runBlocking {
        delay(10000)
        println("Hellodddd ${currentThreadName()}")
    }
    println("no block ${currentThreadName()}")
    Thread.sleep(20000) // wait for 2 seconds
    println("Stop ${currentThreadName()}")
}