#line plot 
import matplotlib.pyplot as plt

x = [1, 2, 3, 4, 5]
y = [10, 20, 15, 25, 30]

plt.plot(x, y)
plt.xlabel("X values")
plt.ylabel("Y values")
plt.title("Simple Line Plot")
plt.show()


#bar chart
import matplotlib.pyplot as plt

subjects = ["Python", "Java", "DBMS", "AI"]
marks = [85, 75, 90, 80]

plt.bar(subjects, marks)
plt.xlabel("Subjects")
plt.ylabel("Marks")
plt.title("Student Marks")
plt.show()

#scatter
import matplotlib.pyplot as plt

x = [1, 2, 3, 4, 5]
y = [2, 4, 5, 7, 9]

plt.scatterplot(x=x, y=y)
plt.title("Scatter Plot")
plt.show()


#histogram
import matplotlib.pyplot as plt

marks = [45, 55, 60, 65, 70, 70, 75, 80, 85, 90]

plr.histplot(marks, bins=5)
plt.xlabel("Marks")
plt.ylabel("Number of Students")
plt.title("Marks Distribution")
plt.show()