package demo

import java.math.BigDecimal

data class Money(val amount: BigDecimal, val currency: String)



fun sendPayment(money: Money, message: String = "") {
    println("Sending ${money.amount}")
}

fun sum(x: Int, y: Int) = x + y // single expression function


fun BigDecimal.percent(percentage: Int) = this.multiply(BigDecimal(percentage)).divide(100.db)// available in the demo package
infix fun Int.percenOf(money: Money) = money.amount.multiply(BigDecimal(this)).divide(100.db)

operator fun Money.plus(money: Money) =
        if (currency === money.currency) {
            Money(amount + money.amount, currency)
        } else
            throw IllegalArgumentException("We're gonna have a problem here!")

// function expression
fun convertToDollars(money: Money) = when(money.currency) {
        "$" -> money
        "EUR" -> Money(money.amount * BigDecimal(1.10), "$")
        else -> throw IllegalArgumentException("Not the currency you're interested in!")
}

//fun javaMoney(money: JavaMoney?) {
//    println("${money?.amount}")//if money is null, then do something
//}
//
//class JavaMoney {
//    val  amount: BigDecimal = null!!
//
//}

fun findEmail(users: List<User>, predicate: (String) -> (Boolean)): List<User> {
    TODO("later")
}

fun main(args: Array<String>) {
    val tickets = Money(100.db, "$")

    val popcorn = tickets.copy(100.db, "$")
    
    val bd1 = BigDecimal(100)
    val bd2 = 100.db

    7 percenOf popcorn

    bd1.percent(7)
    // property comparision(verse property comparision)
    sendPayment(message = "Goodtickets", money = tickets)
    if (tickets != popcorn) {
        print("They are different")
    }
    val costs = tickets + popcorn //operator override for money
    // you should shy away from, we don't enforce immutability in Kotlin, but we kind of do recommend it
    // i cannot assign null in Kotlin because Kotlin tries to get rid of the null pointer exception by saying that types aren't nullible by default

    var train : Money? = Money(100.db, "$")

    train = null




    val users = userFromJSONFile("user.json")
    findEmail(users) {
        it.endsWith(".com")
    }
    val ( id, _, _ ) = users.filter { it.email.endsWith(".com") }
            .sortedBy { it.id }.first()
//            .map{ it.email to it.username} // A infix function to Pair
    print(id)
}

private val  Int.db: BigDecimal
    get() = BigDecimal(this)
