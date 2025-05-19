x = ('apple', 'banana', 'cherry')
y = enumerate(x, 10)
# enumerate(iterable(here, x), start(here, 10)
print(list(y))

a = ("John", "Charles", "Mike")
b = ("Jenny", "Christy", "Monica", "Alex")
x = zip(a, b)
# zip(iterator1, iterator2, iterator3 ...)
# If the passed iterables have different lengths, the iterable with the least items decides the length of the new iterator.
# use the tuple() function to display a readable version of the result:
print(tuple(x))
