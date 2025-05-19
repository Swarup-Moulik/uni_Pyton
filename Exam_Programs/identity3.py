import numpy as np

d = int(input("Enter the dimension of square matrix :- "))
mc = []
for i in range(d):
    mr = []
    for j in range(d):
        v = int(input(f"Enter value for [{i+1}][{j+1}] :-"))
        mr.append(v)
    mc.append(mr)

ar = np.array(mc)
print(ar)

# hard coded way
arr = np.array([[1,0,0], [0,1,0], [0,0,1]])
for r in arr:
    for c in r:
        print(c, end=" ")
    print()
