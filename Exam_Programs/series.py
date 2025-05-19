n = int(input("Enter the number of terms :- "))
s_sum = 0
for i in range(1, n + 1):
    s_sum += i / (i + 1)
print(f"Sum of the series :- {s_sum}")
