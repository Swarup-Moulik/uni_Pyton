r = int(input("Enter the number of rows :- "))
for i in range(1, r+1):
    num = i
    for j in range(1, i+1):
        print(num, end="\t")
        num -= 1
    print()