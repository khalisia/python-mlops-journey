import pandas as pd

FILE_NAME = "employees_dirty.csv"

def load_dataset():
    """Load the dataset from csv"""
    return pd.read_csv(FILE_NAME)

def inspect_dataset(df):
    """Display basic information about the dataset."""
    print("\n==== DATASET ====")
    print(df)

    print("\n==== DATA TYPES ====")
    print(df.dtypes)

    print("\n==== MISSING VALUES =====")
    print(df.isnull().sum())

    print("\n===== DUPLICATES =====")
    print(df.duplicated().sum())

def clean_dataset(df):
    """Clean missing values, invalid values and duplicates."""

    # Convert Salary to Numeric
    df["Salary"] = pd.to_numeric(df["Salary"], errors= "coerce")

# Fill missing numeric values
    df["Age"] = df["Age"].fillna(df["Age"].mean())
    df["Salary"] = df["Salary"].fillna(df["Salary"].median())

# Fill missing text values
    df["Department"] = df["Department"].fillna("Unknown")

#Remove Duplicate rows

    df = df.drop_duplicates()

    return df

def main():
    df = load_dataset()

    print("===== BEFORE CLEANING =====")
    inspect_dataset(df)

    df = clean_dataset(df)

    print("\n===== AFTER CLEANING =====")
    print(df)

    print("\n ===== MISSING AFTER CLEANING =====")
    print(df.isnull().sum())

    print("\n===== DUPLICATES AFTER CLEANING =====")
    print(df.duplicated().sum())

if __name__ == "__main__":
    main()