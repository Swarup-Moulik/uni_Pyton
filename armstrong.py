print("The Armstrong numbers between 1 to 1000 :- ", end=" ")
for i in range(1001):
    num = i
    dig = len(str(num))
    sum_dig = 0
    for j in str(num):
        sum_dig += int(j) ** dig
    if sum_dig == i:
        print(i, end=" ")

