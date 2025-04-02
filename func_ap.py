def series(n):
    sum = 0
    for i in range(n + 1):
        sum += i
    return sum


N = int(input("Enter the number of terms :-"))
ans = series(N)
print("The sum of the series :- ", ans)
