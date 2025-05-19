def divisible(x):
    if x % 3 == 0 or x % 6 == 0:
        return True
    else:
        return False


l = [i for i in range(1, 51)]
print("The list :- ", *l)

# normal way
d = filter(divisible, l)
print("Numbers divisible by 3 or 6 :- ")
for j in d:
    print(j, end=" ")

print()

# lambda way
print("Numbers divisible by 3 or 6 using lambda function:- ")
div = list(filter(lambda x: x % 3 == 0 or x % 6 == 0, l))
print(*div)
