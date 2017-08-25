package basic

inline fun <reified T> List<T>.filterIsInstance() = this.filter { it is T }

fun main(args: Array<String>) {
    val list = listOf(1, 2f, 3, 4f)
    val ints = list.filterIsInstance<Int>()
    println(ints)
}