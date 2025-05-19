def even(x):
    if x % 2 == 0:
        return True
    else:
        return False


n = int(input("Enter the number of items in the list :- "))
l = []
for i in range(n):
    num = int(input(f"Enter the number at position {i + 1} :- "))
    l.append(num)

# normal way
e = filter(even, l)
print("Even numbers :- ")
for j in e:
    print(j, end=" ")

print()

# lambda way
print("Even numbers using lambda function :- ")
even = list(filter(lambda x: x % 2 == 0, l))
print(*even)
