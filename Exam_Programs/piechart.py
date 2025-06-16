import matplotlib.pyplot as plt

an = int(input("Enter the number of activities :- "))
anm = []
at = []
for i in range(an):
    name = input(f"Enter the name of the activity {i+1}:- ")
    anm.append(name)
    time = int(input(f"Enter the time spent on {anm[i]} :- "))
    at.append(time)
plt.pie(at, labels=anm, startangle=90)
plt.legend(title="Daily Activities :-")
plt.show()
