package demo

import kotlinx.coroutines.experimental.*

fun main(args: Array<String>) {
    println("Start")
    // Start a coroutine
    launch(CommonPool) {
        while (true) {
            delay(1000) //We are using the delay() function that's like Thread.sleep(), but better: it doesn't block a thread, but only suspends the coroutine itself.
            println("Hello") //The thread is returned to the pool while the coroutine is waiting, and when the waiting is done, the coroutine resumes on a free thread in the pool.
        }
    }
//    Thread.sleep(20000) // wait for 2 seconds
    runBlocking {
        delay(20000)
    }
    println("Stop")
}