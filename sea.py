import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
df={
    "Marks":[10,20,30,40],
    "Name":['A','B','C','D']
}
# sns.lineplot(x="Marks",y="Name",data=df)
# sns.histplot(x="Marks",y="Name",data=df)
# sns.scatterplot(x="Marks",y="Name",data=df)
sns.displot(x="Marks",y="Name",data=df)
plt.show()
