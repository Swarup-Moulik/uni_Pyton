def student_sports(name, *sports):
    print(f"Student Name :- {name}")
    print("Favourite Sports :- ",", ".join(sports) if sports else "None")


student_sports("Rahul", "Cricket", "Football")
student_sports("Anjali", "Tennis")
student_sports("Meena")