x = int(input("Enter the 1st number :- "))
y = int(input("Enter the 2nd number :- "))
print("\tBefore Swapping\t")
print("The 1st number :- ", x)
print("The 2nd number :- ", y)
x = x ^ y
y = y ^ x
x = y ^ x
print("\tAfter Swapping\t")
print("The 1st number :- ", x)
print("The 2nd number :- ", y)