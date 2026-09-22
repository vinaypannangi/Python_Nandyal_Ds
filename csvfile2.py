import pandas as pd
data={
"Name":["Rahul","Aman","Priya"],
"Departure":["bsc","bsc","bsc"],
"Age":[20,21,20],
"Marks":[85,72,91],
"Attendance":[90,80,95]
}
df=pd.DataFrame(data)
df.to_csv("students.csv",index=False)
print("csv file created successfully.")
new_df=pd.read_csv("students.csv")
print("\nData read from csv:")
print(new_df)