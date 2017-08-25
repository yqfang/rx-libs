package coroutine

import kotlinx.coroutines.experimental.*
import util.currentThreadName
import kotlin.system.measureTimeMillis

fun main(args: Array<String>) = runBlocking<Unit> {
// What if there are no dependencies between invocation of doSomethingUsefulOne and doSomethingUsefulTwo
// and we want to get the answer faster, by doing both concurrently? This is where async comes to help.
// Conceptually, async is just like launch. It starts a separate coroutine which is a light-weight thread
// that works concurrently with all the other coroutines. The difference is that launch returns a Job and
// does not carry any resulting value, while async returns a Deferred -- a light-weight non-blocking future that
// represents a promise to provide a result later. You can use .await() on a deferred value to get its eventual result
// , but Deferred is also a Job, so you can cancel it if needed.

    val time = measureTimeMillis {
        val one = async(CommonPool, CoroutineStart.LAZY) { doSomethingUsefulOne() }
        val two1 = async(CommonPool) { doSomethingUsefulTwo() }
        val two2 = async(CommonPool) { doSomethingUsefulTwo() }
        val two3 = async(CommonPool) { doSomethingUsefulTwo() }
        val two4 = async(CommonPool) { doSomethingUsefulTwo() }
        val two5 = async(CommonPool) { doSomethingUsefulTwo() }
        val two6 = async(CommonPool) { doSomethingUsefulTwo() }
        val two7 = async(CommonPool) { doSomethingUsefulTwo() }
        val two8 = async(CommonPool) { doSomethingUsefulTwo() }
        val two9 = async(CommonPool) { doSomethingUsefulTwo() }
//        println("The answer is ${one.await() + two1.await() + two2.await() + two3.await() + two4.await() + two5.await() + two6.await() + two7.await() + two8.await() + two9.await()}")
    }
    println("Completed in $time ms")
}