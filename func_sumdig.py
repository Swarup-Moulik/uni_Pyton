def sumdig(n):
    sum_digits = 0
    for i in str(num):
        sum_digits += int(i)
    return sum_digits


num = int(input("Enter the number :- "))
sd = sumdig(num)
print("The sum of digits :- ", sd)
