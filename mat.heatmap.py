import matplotlib.pyplot as plt

data = [
    [10, 20, 30],
    [40, 50, 60],
    [70, 80, 90]
]

plt.imshow(data, cmap="hot")
plt.colorbar()
plt.title("Heatmap")
plt.xlabel("Columns")
plt.ylabel("Rows")
plt.show()