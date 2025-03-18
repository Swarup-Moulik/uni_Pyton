s1 = int(input("Enter the 1st side of the triangle :- "))
s2 = int(input("Enter the 2nd side of the triangle :- "))
s3 = int(input("Enter the 3rd side of the triangle :- "))
if s1 == s2 == s3:
    print("Equilateral triangle")
elif s1 == s2 or s2 == s3 or s3 == s1:
    print("Isosceles triangle")
else:
    print("Scalene triangle")


if s1*s1 + s2*s2 == s3*s3 or s2*s2 + s3*s3 == s1*s1 or s1*s1 + s3*s3 == s2*s2:
    print("Right Angled Triangle")
else:
    print("Not a Right Angled Triangle")
