import matplotlib.pyplot as plt

hour_study = [1, 2, 3, 4, 5, 6, 7]
marks = [45, 50, 55, 60, 70, 75, 80]
plt.scatter(hour_study, marks, color="red")
plt.title("Marks vs Time")
plt.xlabel("Time Spent")
plt.ylabel("Marks Got")
plt.grid(True)
plt.show()