import csv
import logging
from pathlib import Path

# Configure logging
logging.basicConfig(
    filename="expense_tracker.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

CSV_FILE = "expenses.csv"


def initialize_csv():
    """Create the CSV file with a header if it doesn't exist."""
    if not Path(CSV_FILE).exists():
        with open(CSV_FILE, "w", newline="") as file:
            writer = csv.writer(file)
            writer.writerow(["Category", "Amount"])
        logging.info("Created expenses.csv with header.")


def add_expense():
    """Add a new expense to the CSV file."""
    category = input("Enter expense category: ")

    try:
        amount = float(input("Enter amount: "))

        if amount < 0:
            raise ValueError("Amount cannot be negative.")

        with open(CSV_FILE, "a", newline="") as file:
            writer = csv.writer(file)
            writer.writerow([category, amount])

        logging.info(f"Expense added: {category} - KSh {amount}")
        print("Expense added successfully!")

    except ValueError as e:
        logging.error(f"Invalid amount entered: {e}")
        print("Please enter a valid positive number.")


def view_expenses():
    """Display all expenses."""
    try:
        with open(CSV_FILE, "r", newline="") as file:
            reader = csv.reader(file)

            next(reader)  # Skip the header

            print("\nExpenses")
            print("-" * 30)

            empty = True

            for row in reader:
                empty = False
                print(f"Category: {row[0]:15} Amount: KSh {row[1]}")

            if empty:
                print("No expenses recorded.")

        logging.info("Viewed expenses.")

    except FileNotFoundError:
        logging.error("expenses.csv not found.")
        print("No expense file found.")


def summarize_expenses():
    """Calculate and display the total expenses."""
    total = 0

    try:
        with open(CSV_FILE, "r", newline="") as file:
            reader = csv.reader(file)

            next(reader)  # Skip the header

            for row in reader:
                total += float(row[1])

        print(f"\nTotal Expenses: KSh {total:.2f}")
        logging.info(f"Calculated total expenses: KSh {total:.2f}")

    except FileNotFoundError:
        logging.error("expenses.csv not found.")
        print("No expense file found.")

    except ValueError:
        logging.error("Invalid data found in expenses.csv.")
        print("The expense file contains invalid data.")


def main():
    initialize_csv()
    logging.info("Expense Tracker started.")

    while True:
        print("\n===== Expense Tracker =====")
        print("1. Add Expense")
        print("2. View Expenses")
        print("3. Show Total Expenses")
        print("4. Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            add_expense()

        elif choice == "2":
            view_expenses()

        elif choice == "3":
            summarize_expenses()

        elif choice == "4":
            logging.info("Expense Tracker closed.")
            print("Goodbye!")
            break

        else:
            logging.warning(f"Invalid menu choice: {choice}")
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()