r = int(input("Enter the number of rows :- "))
num = r
for i in range(0, r):
    for j in range(r-i, 0, -1):
        print(num, end="\t")
    num = num - 1
    print()