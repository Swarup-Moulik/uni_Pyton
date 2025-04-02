n = int(input("Enter the number of terms :- "))
sum_series = 0
for i in range(1, n+1):
    sum_term = 0
    for j in range(i+1):
        sum_term += j
    sum_series += sum_term
print("The sum of the series :- ", sum_series)