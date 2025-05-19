def square(x):
    return x**2


n = int(input("Enter the number of items in the list :- "))
l = []
for i in range(n):
    num = int(input(f"Enter the number at position {i+1} :- "))
    l.append(num)

# normal way
e = map(square,l)
print("Squared numbers :- ")
for j in e:
    print(j, end=" ")

print()

# lambda way
print("Squared numbers using lambda function :- ")
squares = list(map(lambda x: x ** 2, l))
print(*squares)

