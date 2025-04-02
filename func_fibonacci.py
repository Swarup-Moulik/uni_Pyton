def fibonacci(n):
    a, b = 0, 1
    for i in range(N):
        c = a + b
        print(a, end=" ")
        a = b
        b = c


N = int(input("Enter the number of terms :- "))
print("The fibonacci series :- ", end=" ")
fibonacci(N)