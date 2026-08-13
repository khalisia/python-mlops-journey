import pandas as pd

df = pd.read_csv("students.csv")

# 2. Strip hidden spaces from all column names
df.columns = df.columns.str.strip()

# 3. Print loaded column names for debugging
print("Loaded Columns:", df.columns.tolist())

print("Student Data")
print(df)

print("\n First 5 students:")
print(df.head())

print("\nAverage Score:")
print(df["Score"].mean())

print("\nHighest Score:")
print(df["Score"].max())

print("\n Lowest Score")
print(df["Score"].min())