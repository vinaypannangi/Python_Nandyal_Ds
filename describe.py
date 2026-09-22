import pandas as pd
data={
"name":['a','b','c','d'],
"age":[20,30,40,50],
"marks":[100,90,120,160]}
d1=pd.DataFrame(data)
print(d1)
d2=d1[d1["marks"] <= 150]
print(d2)
print(d1["age"].mean())
print(d1.shape)
print()
print(d1.columns)
print()
print(d1.index)
print()
print(d1.dtypes)
print(d1.describe)