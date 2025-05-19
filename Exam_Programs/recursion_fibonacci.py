def fibo(num):
    if num <= 1:
        return num
    return fibo(num - 1) + fibo(num - 2)


n = int(input("Enter the number of terms :- "))
print("The fibonacci series :- ")
for i in range(n):
    print(fibo(i), end=" ")