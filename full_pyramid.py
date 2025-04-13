r = int(input("Enter the number of rows :- "))
for i in range(1, r+1):
    for k in range(r-i, 0, -1):
        print(" ", end="\t")
    a = i
    for j in range(1, i+1):
        print(a, end="\t")
        a += 1
    b = a - 1
    for l in range(1, i):
        b -= 1
        print(b, end="\t")
    print()