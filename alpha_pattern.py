r = int(input("Enter the number of rows :- "))
for i in range(1, r+1):
    for j in range(i):
        print(i, end="\t")
    print()