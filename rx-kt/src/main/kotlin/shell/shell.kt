package shell

import io.reactivex.Observable
import io.reactivex.rxkotlin.subscribeBy
import kotlinx.coroutines.experimental.*
import java.io.BufferedReader
import java.io.InputStream
import java.io.InputStreamReader

fun main(args: Array<String>) = runBlocking<Unit> {
    val process: Process = asyncProcessStreamJob(process = {
        ProcessBuilder("sh","/Users/yqfang/develop/github/open/rx/rx-kt/src/main/resources/plainShell.sh").start()
    }
        , onProcessStartSuccess = { println("the job is started!") }
        , onStdOutNext = { println(it) }
        , onStdErrNext = { println("from stderr: $it") }
        , onUnexpectedError = { println("from unexpectederr: $it") }
        , onProcessEnd = {
            async(CommonPool) {
                println("ENDCODE: ${it.exitValue()}")
            }
        }
        ,timeout = {15000}
    )

    println("我没有被阻塞")
    delay(23000)
}

enum class StreamType {
    STDOUT, STDERR
}

suspend fun getStreamObservable(process: Process, streamType: StreamType = StreamType.STDOUT): Observable<String> {
    val source: Observable<String> = Observable.create {
        try {
            val stream: InputStream = if(streamType === StreamType.STDOUT) process.inputStream else process.errorStream
            val inputStream = BufferedReader(InputStreamReader(stream))
            var line: String? = inputStream.readLine()
            while (line != null) {
                it.onNext(line)
                line = inputStream.readLine()
            }
            it.onComplete()
        } catch (e: Throwable) {
            it.onError(e)
        }
    }
    return source;
}
fun asyncProcessStreamJob(timeout: () -> Long = {Long.MAX_VALUE}, onProcessStartSuccess: (Process) -> Unit = {}, process: () -> Process, onStdOutNext: (Any) -> Unit = {}, onStdErrNext: (Any) -> Unit = {}, onProcessEnd: (Process) -> Unit = {}, onUnexpectedError: (Throwable) -> Unit = {}): Process {
    val process: Process = process()
    val timeoutValue = timeout()
    try {

        if(process.isAlive) {
            onProcessStartSuccess(process)
            async(CommonPool) {
                delay(timeoutValue)
                onUnexpectedError(Throwable("timeout: $timeoutValue"))
                process.destroy()
            }
        }
        async(CommonPool){
            getStreamObservable(process, StreamType.STDOUT).subscribeBy(onNext = onStdOutNext, onError = onUnexpectedError, onComplete = { onProcessEnd(process) })
        }
        async(CommonPool){
            getStreamObservable(process, StreamType.STDERR).subscribeBy(onNext = onStdErrNext, onError = onUnexpectedError)
        }
    } catch (e: Throwable) {
        onUnexpectedError(e)
        if (process.isAlive) {
            process.destroy()
        }
    }
    return process
}
