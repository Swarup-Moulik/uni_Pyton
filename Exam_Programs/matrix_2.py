import numpy as np

row = int(input("Enter the row of matrix :- "))
col = int(input("Enter the column of matrix :- "))
mc = []
for i in range(row):
    mr = []
    for j in range(col):
        v = int(input(f"Enter value 2 for [{i+1}][{j+1}] :-"))
        mr.append(v)
    mc.append(mr)

ar = np.array(mc)
for r in ar:
    for c in r:
        print(c, end=" ")
    print()