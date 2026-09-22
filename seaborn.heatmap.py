import seaborn as sns
import matplotlib.pyplot as plt

data = [
    [80, 70, 90],
    [60, 85, 75],
    [90, 95, 80]
]

sns.heatmap(data, annot=True)
plt.title("Marks Heatmap")
plt.show()