n = int(input("Enter the number of items in the list :- "))
l1 = []
l2 = []
f = 0
for i in range(n):
    num = int(input(f"Enter the number at position {i + 1} :- "))
    l1.append(num)
for i in l1:
    if i not in l2:
        l2.append(i)

print("No duplicate list :- ", *l2)
