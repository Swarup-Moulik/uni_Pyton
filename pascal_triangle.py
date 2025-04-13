r = int(input("Enter number of rows: "))
array = [[0] * (r * 2 - 1) for i in range(r)]
m = r - 1
for i in range(r):
    array[i][m - i] = 1
    array[i][m + i] = 1
    if i > 0:
        for j in range(r - i, m + i):
            array[i][j] = array[i - 1][j - 1] + array[i - 1][j + 1]
print("Pascal's Triangle:")
for row in array:
    for num in row:
        if num != 0:
            print(num, end=' ')
        else:
            print(' ', end=' ')
    print()

