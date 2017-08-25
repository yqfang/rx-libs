package util

import java.util.*

fun currentThreadName(): String {
    return Thread.currentThread().name
}

fun getFilePath(fileName: String): String {
    return String::class.java.getResource(fileName).path
}