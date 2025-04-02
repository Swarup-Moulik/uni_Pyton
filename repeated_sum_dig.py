num = int(input("Enter the number :- "))
sum_digits = 0
while len(str(num)) > 1:
    for i in str(num):
        sum_digits += int(i)
    num = sum_digits
    sum_digits = 0
print("The single digit :- ", num)