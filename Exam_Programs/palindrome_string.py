word = input("Enter the string :- ")
rev_word = word[::-1]
if word == rev_word:
    print("Palindrome Sting :- ", word)
else:
    print("Not a Palindrome sting :- ", word)