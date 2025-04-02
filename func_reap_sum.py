def reap(n):
    sum_digits = 0
    while len(str(n)) > 1:
        for i in str(n):
            sum_digits += int(i)
        n = sum_digits
        sum_digits = 0
    return n


num = int(input("Enter the number :- "))
sd = reap(num)
print("The single digit :- ", sd)