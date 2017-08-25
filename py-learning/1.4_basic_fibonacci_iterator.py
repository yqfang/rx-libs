from itertools import islice
class fib:
    def __init__(self):
        self.prev = 0
        self.curr = 1

    def __iter__(self):
        return self

    def next(self):
        value = self.curr
        self.curr += self.prev
        self.prev = value
        return value

f = fib()
# [1, 1, 2, 3, 5, 8, 13, 21, 34, 55]
print(list(islice(f, 0, 10)))
# [89, 144, 233, 377, 610, 987, 1597, 2584, 4181, 6765] so it seems weird
print(list(islice(f, 0, 10)))


class fib2:
    def __init__(self):
        pass

    def __iter__(self):
        class fib_iter():
            def __init__(self):
                self.prev = 0
                self.curr = 1
            def __iter__(self):
                # Iterators are iterables too.
                # Adding this functions to make them so.
                return self
            def next(self):
                value = self.curr
                self.curr += self.prev
                self.prev = value
                return value
        return fib_iter()
f2 = fib2()
# [1, 1, 2, 3, 5, 8, 13, 21, 34, 55]
print(list(islice(f2, 0, 10)))
# [1, 1, 2, 3, 5, 8, 13, 21, 34, 55] it seems ok
print(list(islice(f2, 0, 10)))





