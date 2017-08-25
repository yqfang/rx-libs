package redis

import redis.clients.jedis.Jedis

fun main(args: Array<String>) {
    val jedis:Jedis = Jedis("localhost")
    println(jedis.ping())
    jedis.set("runoobkey", "www.runoob.com");
    println("redis 存储的字符串为: "+ jedis.get("runoobkey"));

    //存储数据到列表中
    jedis.lpush("site-list", "Runoob")
    jedis.lpush("site-list", "Google")
    jedis.lpush("site-list", "Taobao")
    // 获取存储的数据并输出
    val list = jedis.lrange("site-list", 0, 2)
    for (i in list.indices) {
        println("列表项为: " + list[i])
    }

    // 获取数据并输出
    val keys = jedis.keys("*")
    val it = keys.iterator()
    while (it.hasNext()) {
        val key = it.next()
        println(key)
    }
}