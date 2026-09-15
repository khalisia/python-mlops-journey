import pandas as pd

#Loading the csv
FILE_NAME = "sales.csv"

def load_data():
    """Load the csv file."""
    return pd.read_csv(FILE_NAME)

#Dataset statistics
def show_statistics(df):
    """Display basic statistics about the dataset."""

    print("\n===== STATISTICS ======")

    print(f"Rows: {df.shape[0]}")
    print(f"Columns: {df.shape[1]}")

    print(f"Total Sales : Ksh {df['Amount'].sum():,.2f}")
    print(f"Average Sale : Ksh {df['Amount'].mean():,.2f}")
    print(f"Highest Sale : Ksh {df['Amount'].max():,.2f}")
    print(f"Lowest Sale : Ksh {df['Amount'].sum():,.2f}")

#Sales summary

def show_category_summary(df):
    """Display sales grouped by category"""

    print("\n===== SALES BY CATEGORY =====")

    result = df.groupby("Category")["Amount"].sum()

    print(result)

#Filtering

def show_high_value_sales(df):

    """Display sales above a specified amount."""

    amount = float(input("\nEnter minimum sale amount: "))

    result = df[df["Amount"] > amount]

    print(f"\n===== SALES ABOVE KSh {amount:,.2f} =====")

    print(result)

#Filter by category

def filter_by_category(df):
    """Display sales fron a specific category"""

    category = input("\nEnter category: ").strip()

    result = df[ df["Category"].str.lower == category.lower()]

    print(f"\n===== {category.upper()} SALES =====")

    print(result)

def main():
    """Run the csv analytics tool"""

    df = load_data()

    print("================================")
    print("       CSV ANALYTICS TOOL")
    print("================================")

    print("\n===== DATASET =====")
    print(df)

    show_statistics(df)
    show_category_summary(df)
    show_high_value_sales(df)
    filter_by_category(df)

if __name__ == "__main__":
    main()
    