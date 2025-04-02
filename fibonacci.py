N = int(input("Enter the number of terms :-"))
a, b = 0, 1
print("The fibonacci series :- ", end=" ")
for i in range(N):
    c = a + b
    print(a, end=" ")
    a = b
    b = c
