# Addition function
def add(a, b):
    return a + b

# Subtraction function
def subtract(a, b):
    return a - b

# Multiplication function
def multiply(a, b):
    return a * b

# Division function
def divide(a, b):
    if b == 0:
        return "Error: Division by zero is undefined."
    return a / b

# Combining all operations into a single function
while True:
    print("=== Function Calculator ===")

    num1 = float(input("Enter the first number: "))
    operator = input("Enter the operator (+, -, *, /): ")
    num2 = float(input("Enter the second number: "))

    if operator == '+':
        print(f"Result: {add(num1, num2)}")
    elif operator == "-":
        print(f"Result: {subtract(num1, num2)}")
    elif operator == "*":
        print(f"Result: {multiply(num1, num2)}")
    elif operator == "/":
        print(f"Result: {divide(num1, num2)}")
    else:
        print("Error: Invalid operator.")

    again = input("Do you want to perform another calculation? (yes/no): ").strip().lower()
    if again != "yes":
        print("Goodbye!")
        break