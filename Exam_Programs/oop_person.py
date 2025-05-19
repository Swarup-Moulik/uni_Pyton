class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display_person(self):
        print("Name :- ", self.name)
        print("Age :- ", self.age)


class Student(Person):
    def __init__(self, name, age, roll, marks):
        super().__init__(name, age)
        self.roll = roll
        self.marks = marks

    def display_student(self):
        print("-- Student Details --")
        self.display_person()
        print("Roll No. :-", self.roll)
        print("Marks :- ", self.marks)
        print("-----")


class Teacher(Person):
    def __init__(self, name, age, subject, experience):
        super().__init__(name, age)
        self.subject = subject
        self.experience = experience

    def display_teacher(self):
        print("-- Teacher Details --")
        self.display_person()
        print("Subject :-", self.subject)
        print("Experience :- ", self.experience)
        print("-----")


student1 = Student("Rahul", 20, 25, 88)
teacher1 = Teacher("Mrs. Sharma", 45, "Mathematics", 20)

student1.display_student()
teacher1.display_teacher()
