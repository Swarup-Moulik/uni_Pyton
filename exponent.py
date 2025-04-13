num = int(input("Enter the number :- "))
index = int(input("Enter the power :- "))
f = 1
for i in range(0, index, 1):
    f *= num
print("The result :- ", f)

