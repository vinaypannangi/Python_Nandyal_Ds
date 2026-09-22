#1: Line Graph
import matplotlib.pyplot as plt

x = [1, 2, 3, 4, 5]
y = [10, 20, 15, 30, 25]

plt.plot(x, y, marker='o')
plt.xlabel("X Values")
plt.ylabel("Y Values")
plt.title("Simple Line Graph")
plt.show()


#2: Bar Graph
import matplotlib.pyplot as plt

subjects = ["Maths", "Science", "English", "Python"]
marks = [85, 90, 75, 95]

plt.bar(subjects, marks)
plt.xlabel("Subjects")
plt.ylabel("Marks")
plt.title("Student Marks")
plt.show()