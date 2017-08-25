package `class`

data class user(val name: String)

fun main(args: Array<String>) {
    var user1 = user("yqfang")
    var user2 = user("yqfang")
    println(user1.equals(user2))
    println(user1)
}