import matplotlib.pyplot as plt

ns = int(input("Enter the number of subjects :- "))
snm = []
smk = []
for i in range(ns):
    sub_name = input("Enter the name of subject :- ")
    snm.append(sub_name)
    marks = int(input(f"Marks got in {snm[i]} :- "))
    smk.append(marks)
plt.bar(snm, smk, color="blue")
plt.title("Report Card")
plt.xlabel("Subject Name")
plt.ylabel("Marks Got")
plt.ylim(60, 100)
plt.show()