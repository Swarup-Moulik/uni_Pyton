marks = int(input("Enter the marks of the subject :- "))
if 85 <= marks <= 100:
    print("Grade A")
elif 60 <= marks < 85:
    print("Grade B+")
elif 40 <= marks < 60:
    print("Grade B")
elif 30 <= marks < 40:
    print("Grade C")
else:
    print("Failed")
