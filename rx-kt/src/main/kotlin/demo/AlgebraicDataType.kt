package demo

sealed class UserResult // just see the sealed and open
data class Success(val users: List<User>): UserResult()// all class are essentially final
data class Failure(val message: String): UserResult()

fun retrieveUsers(): UserResult {
    return Success(userFromJSONFile("user.json"))
}
// Kotlin is here, Life is great and everythong will be ok
fun main(args: Array<String>) {
    val result = retrieveUsers()
    val values = generateSequence(1) {
        it * 10
    }
    values.take(10).forEach { println(it) }
    val users = userFromJSONFile("user.json").asSequence() // lazy evaluation
    users.take(2).forEach { println(it) }
    when(result) {
        is Success -> result.users.forEach{println(it.username)} // smart casting
        is Failure -> println(result.message)
    }
}