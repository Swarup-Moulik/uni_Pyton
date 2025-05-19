age = int(input("Enter the age :- "))
if age < 12:
    print("The person in Child")
elif 12 < age < 18:
    print("The person is Teenager")
elif 18 < age < 60:
    print("The person is Adult")
elif age > 60:
    print("The person is Senior Citizen")
else:
    print("Wrong Input")