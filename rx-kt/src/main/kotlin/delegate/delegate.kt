package delegate

interface Base {
    fun print()
}

class BaseImpl(val x: Int) : Base {
    override fun print() {
        print(x)
    }
}

class Derived(b: Base) : Base by b {
// Note that overrides work as you might expect:
// The compiler will use your override implementations instead of those in the delegate object.
// If we were to add override fun print() { print("abc") } to Derived, the program would print "abc" instead of "10".
    override fun print() {
        print("dddd")
    }
}

fun main(args: Array<String>) {
    val b = BaseImpl(10)
    Derived(b).print() // prints 10
}