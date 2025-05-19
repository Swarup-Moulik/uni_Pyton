def simple_interest(p1=1000, r1=10, t1=5):
    si = p1 * r1 * t1 / 100
    print("The simple interest = ", si)


p = float(input("Enter the principal :- "))
r = float(input("Enter the rate of interest :- "))
t = int(input("Enter the time period :- "))
print("Default values :- ", end=" ")
simple_interest()
print("Positional Arguments :- ", end=" ")
simple_interest(p, r, t)
print("Keyword Arguments :- ", end=" ")
simple_interest(r1=2, t1=20, p1=25000)
print("One Keyword Argument :- ", end=" ")
simple_interest(t1=13)
