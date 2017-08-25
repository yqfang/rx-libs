package delegate

fun main(args: Array<String>) {
    val lazyValue: String by lazy {
        println("computed")
        println("computed")
        println("computed")
        println("computed")
        println("computed")
        println("computed")
        println("computed")
        "hello"
    }
    println(lazyValue)
    println(lazyValue)
}