print("The odd non prime numbers between 10 to 100 :- ", end=" ")
for i in range(11, 101, 2):
    num = i
    f = 1
    for j in range(2, int(num / 2) + 1):
        if num % j == 0:
            f = 0
            break
    if f == 0:
        print(i, end=" ")