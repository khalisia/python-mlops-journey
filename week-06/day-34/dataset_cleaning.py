import pandas as pd
df = pd.read_csv("employees_dirty.csv")
print(df)

#   Finding missing data

print(df.isnull)

#Count missing values
print(df.isnull().sum())

#Remove Missing Rows
clean_df = df.dropna()
print(clean_df)

#Fill Missing Values
df["Age"] = df["Age"].fillna(df["Age"].mean())
#Filling missing department
df["Department"] = df["Department"].fillna("Unknown")
#Convert Salary to a Number
df["Salary"] = pd.to_numeric(df["Salary"], errors = "coerce")
#Fill the Invalid Salary
df["Salary"] = df["Salary"].fillna(df["Salary"].median())
print(df.duplicated())
df = df.drop_duplicates()