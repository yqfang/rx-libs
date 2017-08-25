from itertools import islice
def fib():
    prev, curr = 0, 1
    while True:
        yield curr
        prev, curr = curr, prev + curr

# Now when f = fib() is called, the generator (the factory) is instantiated and returned. No code will be executed at this point: the generator starts in an idle state initially. To be explicit: the line prev, curr = 0, 1 is not executed yet.
f = fib()
# Any generator also is an iterator (not vice versa!);
# Any generator, therefore, is a factory that lazily produces values.

# Then, this generator instance is wrapped in an islice(). This is itself also an iterator, so idle initially. Nothing happens, still.
# Then, this iterator is wrapped in a list(), which will consume all of its arguments and build a list from it. To do so, it will start calling next() on the islice() instance, which in turn will start calling next() on our f instance.
# This happens until the output list is 10 elements long and when list() asks islice() for the 11th value, islice() will raise a StopIteration exception, indicating that the end has been reached,
print (list(islice(f, 0, 10)))

print (list(islice(f, 0, 10)))

print(f.next())