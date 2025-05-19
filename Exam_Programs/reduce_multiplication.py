from functools import reduce


def multiply(x, y):
    return x * y


n = int(input("Enter the number of items in the list :- "))
l = []
for i in range(n):
    num = int(input(f"Enter the number at position {i + 1} :- "))
    l.append(num)

# normal way
product = reduce(multiply, l)
print("The multiplied values :- ", product)

print()

# lambda way
mul = reduce(lambda x, y: x*y, l)
print("The multiplied values using lambda function :- ", mul)
