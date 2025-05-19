num = int(input("Enter the number :- "))
result = lambda x: "Even" if x % 2 == 0 else "Odd"
print("The number is ", result(num))