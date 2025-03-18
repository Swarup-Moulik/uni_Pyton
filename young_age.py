age1 = int(input("Enter the age of Dip :- "))
age2 = int(input("Enter the age of Rahul :- "))
age3 = int(input("Enter the age of Tamal :- "))
if age1 < age2 and age1 < age3:
    print("Dip is youngest")
elif age2 < age1 and age2 < age3:
    print("Rahul is youngest")
else:
    print("Tamal in youngest")