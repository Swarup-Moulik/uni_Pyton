def palin(num):
    rev_num = num[::-1]
    if num == rev_num:
        print(f"{num} is Palindrome number.")
    else:
        print(f"{num} is not a Palindrome number.")


n = input("Enter the number :- ")
palin(n)
