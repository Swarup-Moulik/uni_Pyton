n = int(input("Enter the value of iterations :- "))
sum = 0
for i in range(1, n + 1):
    sum += i / (i + 1)
print("The result :- ", sum)
