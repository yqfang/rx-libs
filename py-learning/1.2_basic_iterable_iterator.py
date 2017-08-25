# The built-in function iter takes an iterable object and returns an iterator.
x = iter([1, 2, 3])
print(x)

# Each time we call the next method on the iterator gives us the next element. If there are no more elements, it raises a StopIteration.
print(x.next())
print(x.next())


# The __iter__ method is what makes an object iterable
class zrange:
    def __init__(self, n):
        self.n = n

    def __iter__(self):
        return zrange_iter(self.n)


class zrange_iter:
    def __init__(self, n):
        self.i = 0
        self.n = n

    def __iter__(self):
        # Iterators are iterables too.
        # Adding this functions to make them so.
        return self

    def next(self):
        if self.i < self.n:
            i = self.i
            self.i += 1
            return i
        else:
            raise StopIteration()

r = zrange(5)
print(list(r))

print(iter(zrange(4)).next())