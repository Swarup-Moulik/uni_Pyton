calls = int(input("Enter the number of calls :- "))
if calls <= 100:
    bill = 100
    print("Bill :- ", bill)
elif 100 < calls <= 500:
    bill = 100 + (calls-100/50) * 5
    print("Bill :- ", bill)
else:
    bill = 100 + (400/50) * 5 + (calls-500)*1.25
    print("Bill :- ", bill)