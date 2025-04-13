r = int(input("Enter the number of rows :- "))
for i in range(0, r):
    for j in range(r-i, 0, -1):
        print("*", end="\t")
    print()