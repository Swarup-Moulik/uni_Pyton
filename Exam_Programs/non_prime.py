def isPrime(num):
    for j in range(2, num // 2 + 1):
        if num % j == 0:
            return False
    return True


print("Odd Non Prime numbers between 1 to 50 :- ")
for i in range(1, 50, 2):
    prime = isPrime(i)
    if not prime:
        print(i, end=" ")
