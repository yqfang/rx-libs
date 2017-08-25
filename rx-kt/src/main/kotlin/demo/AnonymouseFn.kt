package demo

fun <T> top(collection : Collection<T>, less: (T, T) -> Boolean): T? {
    var top: T? = null
    for (it in collection) {
        if (top == null || less(top, it))
            top = it
    }
    return top
}

//why anonymous funcion
//Anonymous Functions
//
//One thing missing from the lambda expression syntax presented above is the ability to specify the return type of the function. In most cases, this is unnecessary because the return type can be inferred automatically. However, if you do need to specify it explicitly, you can use an alternative syntax: an anonymous function.

fun main(args: Array<String>) {
    val list = listOf<Int>(1, 2, 3, 4, 5)
    println(top(list, fun(x: Int, y: Int) = x < y)) // anony
    println(top(list, fun(x: Int, y: Int): Boolean {
        return x < y
    }))
    val less1 = { x: Int, y: Int -> x < y }
    val less2: (Int, Int) -> Boolean = { x, y -> x < y }
    println(top(list, less1))
    println(top(list, less2))
    println(top(list) {
        x: Int, y: Int ->
        x < y
    })
}