import pandas as pd

FILE_NAME = "sales.csv"

def load_sales():
    """Load sales data from the CSV file."""
    return pd.read_csv(FILE_NAME)

def show_total_sales(df):
    """Display the total sales."""
    total = df["Amount"].sum()

    print(f"\nTotal Sales: Ksh{total:,.2f}")

def show_sales_by_category(df):
    """Display total sales for each category."""
    result = df.groupby("Category")["Amount"].sum()

    print("\nSales by Category")
    print(result)

def show_sales_by_salesperson(df):
    """Display total sales for each sales person."""
    result = df.groupby("Salesperson")["Amount"].sum()

    print("\nSales by Salesperson:")
    print(result)

def show_high_value_sales(df):
    """Display sales above KSh 50,000."""
    result = df[df["Amount"] > 50000]
    print(result)

def show_summary(df):
    """Display a complete sales summary."""
    summary = df.groupby("Category")["Amount"].agg(["sum", "mean", "max", "min", "count"])

    print("\nCategory Summary:")
    print(summary)

def main():
    df = load_sales()

    print("===== SALES ANALYZER =====")

    print("\nSales Data:")
    print(df)

    show_total_sales(df)
    show_sales_by_category(df)
    show_sales_by_salesperson(df)
    show_high_value_sales(df)
    show_summary(df)         

if __name__ == "__main__":
    main()
