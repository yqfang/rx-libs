package persatile

import redis.clients.jedis.Jedis

fun main(args: Array<String>) {
    val jedis: Jedis = Jedis("localhost")
    println(jedis.ping())
}