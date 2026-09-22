import pandas as pd
data={
"Name":["Rahul","Aman","Priya"],
"Age":[20,21,20],
"Marks":[85,72,91]
}
df=pd.DataFrame(data)
df.to_csv("students.csv",index=False)
print("csv file created successfully.")
new_df=pd.read_csv("students.csv")
print("\nData read from csv:")
print(new_df)