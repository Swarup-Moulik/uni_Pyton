num = int(input("Enter the number :- "))
f = 1
if num < 0:
    print("Factorial is not possible.")
elif num == 0:
    print("The factorial = 1")
else:
    while num > 1:
        f *= num
        num = num - 1
    print("The factorial = ", f)
