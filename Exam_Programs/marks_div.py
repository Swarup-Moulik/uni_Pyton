m1 = int(input("Enter the marks in 1st subject :- "))
m2 = int(input("Enter the marks in 2nd subject :- "))
m3 = int(input("Enter the marks in 3rd subject :- "))
total_marks = m1+m2+m3
percentage = float(total_marks/3)
if percentage >= 60:
    print("First division")
elif 50 <= percentage < 60:
    print("Second division")
elif 40 <= percentage < 50:
    print("Third division")
elif percentage < 40:
    print("Fail")