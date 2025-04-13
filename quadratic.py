import math

a = float(input("Enter the first coefficient :- "))
b = float(input("Enter the second coefficient :- "))
c = float(input("Enter the third coefficient :- "))
d = b * b - 4 * a * c
if d > 0:
    r1 = (-b + math.sqrt(d)) / (2 * a)
    r2 = (-b - math.sqrt(d)) / (2 * a)
    print("The 1st root :- ", r1)
    print("The 2nd root :- ", r2)
elif d == 0:
    r = -b / (2 * a)
    print("The only root :- ", r)
else:
    r = -b / (2 * a)
    i = math.sqrt(abs(d)) / (2 * a)
    print(f"The complex root :- {r} + {i:.2f}i")
