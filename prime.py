num = int(input("Enter the number :- "))
f = 1
for i in range(2, int(num/2)+1):
    if num % i == 0:
        f = 0
        break
if f == 1:
    print(f"{num} is prime")
else:
    print(f"{num} is not prime")