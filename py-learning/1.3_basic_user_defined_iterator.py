# The __iter__ method is what makes an object iterable. Behind the scenes, the iter function calls __iter__ method on the given object.

class yrange:
    def __init__(self, n):
        self.i = 0
        self.n = n

    def __iter__(self):
        return self

    def next(self):
        if self.i < self.n:
            i = self.i
            self.i += 1
            return i
        else:
            raise StopIteration()


range = yrange(5)

print(range.next())
print(range.next())

a = yrange(5)
print(list(a))
print(sum(a))