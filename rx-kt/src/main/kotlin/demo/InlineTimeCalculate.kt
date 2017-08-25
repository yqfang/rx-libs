package demo

fun calculate() {
    Thread.sleep(1005)
}

inline fun timeCal(body: () -> Unit): String {
    val start = System.currentTimeMillis()
    try {
        body()
    } finally {
        val end = System.currentTimeMillis()
        return "${end - start} millisecond"
    }
}

fun main(args: Array<String>) {
    print(timeCal(::calculate))
    print(timeCal {
        calculate()
    })
}

