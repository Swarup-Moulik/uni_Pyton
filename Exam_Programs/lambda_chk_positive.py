num = int(input("Enter the number :- "))
result = lambda x: "Positive" if x > 0 else ("Negative" if x < 0 else "Zero")
print("The number is ", result(num))
