class Student:
    count = 0
    def __init__(self, name, roll, marks):
        self.name = name
        self.roll = roll
        self.marks = marks
        Student.count += 1

    def details(self):
        print(f"-- Student {Student.count} Details --")
        print("Name :-", self.name)
        print("Roll No. :-", self.roll)
        print("Marks :- ", self.marks)


student1 = Student("Bobr Kurwa", 23, 340)
student1.details()
student2 = Student("Kitka Kurwa", 32, 430)
student2.details()

