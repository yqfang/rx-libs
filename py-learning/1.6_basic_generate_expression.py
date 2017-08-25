numbers = [1, 2, 3, 4, 5, 6]

lazy_squares = (x * x for x in numbers)
# Note that, because we read the first value from lazy_sqaures with next(), it's state is now at the "second" item, so when we consume it entirely by calling list(), that will only return the partial list of sqaures. (This is just to show the lazy behaviour.) This is as much a generator (and thus, an iterator) as the other examples above.

print(next(lazy_squares))
print(next(lazy_squares))
print(next(lazy_squares))
print(list(lazy_squares))


# Tip to get started with generators: find places in your code where you do the following:
#
# def something():
#     result = []
#     for ... in ...:
#         result.append(x)
#     return result
# And replace it by:
#
# def iter_something():
#     for ... in ...:
#         yield x
