import seaborn as sns
import matplotlib.pyplot as plt

marks = [45, 55, 60, 65, 70, 70, 75, 80, 85, 90]

sns.histplot(marks, bins=5)
plt.xlabel("Marks")
plt.ylabel("Number of Students")
plt.title("Marks Distribution")
plt.show()