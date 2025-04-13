r = int(input("Enter the number of rows :- "))
for i in range(1, r+1):
    for k in range(r-i, 0, -1):
        print(" ", end="\t")
    for j in range(1, i+1):
        print(j, end="\t")
    print()