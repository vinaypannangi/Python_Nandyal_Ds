import pandas as pd
data={
"Name":["Rahul","Aman","Priya"],
"Age":[20,21,20],
"Marks":[85,72,91]
}
df=pd.DataFrame(data)
df.to_json("students.json",orient="records",index=False)
print("JSON  file created successfully.")
new_df=pd.read_json("students.json")
print("\nData read from JSON:")
print(new_df)