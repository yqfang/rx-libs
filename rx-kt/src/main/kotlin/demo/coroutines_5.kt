package demo
import kotlinx.coroutines.experimental.CommonPool
import kotlinx.coroutines.experimental.async
import kotlinx.coroutines.experimental.delay
import kotlinx.coroutines.experimental.runBlocking

suspend fun workload(n: Int): Int {
    delay(1000)
    return n
}

fun main(args: Array<String>) {
    val deferred = async (CommonPool) {
        workload(5)
    }
    runBlocking {
        print(deferred.await())
    }
}