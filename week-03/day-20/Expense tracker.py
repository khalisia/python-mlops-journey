import csv

def add_expense():
    category = input("Category: ")
    amount = float(input("Amount: "))

    with open("expenses.csv","a", newline="") as file:
        writer = csv.writer(file)
        writer.writerow([category, amount])

    print("Expense added successfully!")

def view_expenses():
    try:

        with open("expenses.csv", "r") as file:
            reader = csv.reader(file)

            print("\nExpenses")

            for row in reader:
                print(row)
    except FileNotFoundError:

        print("No expenses found")

def summarize_expenses():
    total = 0

    try:
        with open("expenses.csv", "r") as file:
            reader = csv.reader(file)

            for row in reader:
                total += float(row[1])

        print(f"\nTotal Expenses: Ksh {total}")

    except FileNotFoundError:

        print("No expense data available")

def main():
    while True:
        print("\nExpense Tracker")
        print("1. Add Expense")
        print("2. View Expenses")
        print("3. Show Total")
        print("4. Exit")

        choice = input("Enter an option: ")

        if choice == "1":
            add_expense()

        elif choice == "2":
            view_expenses()

        elif choice == "3":
            summarize_expenses()

        elif choice == "4":
            print("Goodbye!")
            break

        else:
            print("Invalid choice.")

if __name__ == "__main__":
    main()
         


