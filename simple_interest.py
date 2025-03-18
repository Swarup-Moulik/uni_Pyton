p = float(input("Enter the principal :- "))
r = float(input("Enter the rate of interest :- "))
t = int(input("Enter the time period :- "))
si = p*r*t/100
np = si + p
print("The simple interest :- ", si)
print("The new principal :- ", np)