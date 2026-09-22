import seaborn as sns
import matplotlib.pyplot as plt

subjects = ["Python", "Java", "DBMS", "AI"]
marks = [85, 75, 90, 80]

sns.barplot(x=subjects, y=marks)

plt.xlabel("Subjects")
plt.ylabel("Marks")
plt.title("Student Marks")
plt.show()