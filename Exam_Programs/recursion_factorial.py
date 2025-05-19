def fact(n):
    if n < 0:
        return 0
    elif n == 0 or n == 1:
        return 1
    else:
        return n * fact(n - 1)


num = int(input("Enter the number :- "))
f = fact(num)
if f == 0:
    print("Negative number no factorial !")
else:
    print(f"Factorial of {num} :- {f}")
