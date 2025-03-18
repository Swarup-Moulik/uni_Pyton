import math

length = float(input("Enter the length of a rectangle :- "))
breadth = float(input("Enter the breadth of a rectangle :- "))
radius = float(input("Enter the radius of a circle :- "))
perimeter_rect = 2*(length+breadth)
area_rect = length*breadth
circumference_circle = 2*math.pi*radius
area_circle = math.pi*math.pow(radius, 2)
print("The perimeter of rectangle :- ", perimeter_rect)
print("The area of rectangle :- ", area_rect)
print("The circumference of circle :- ", circumference_circle)
print("The area of circle :- ", area_circle)