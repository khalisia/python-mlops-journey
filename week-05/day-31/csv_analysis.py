import pandas as pd

df = pd.read_csv("students.csv")

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