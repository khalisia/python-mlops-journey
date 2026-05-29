
while True:
    print("=== CLI CALCULATOR ===")

    num1 = float(input("Enter the first number: "))
    operator = input("Choose an operator (+, -, *, /): ")
    num2 = float(input("Enter the second number: "))

    if operator == "+":
        result = num1 + num2
        print(f"Result: {result}")

    elif operator == "-":
        result = num1 - num2
        print(f"Result: {result}")

    elif operator == "*":
        result = num1 * num2
        print(f"Result: {result}")

    elif operator == "/":
        if num2 == 0:
            print("Error: Cannot divide by zero.")
        else:
            result = num1 / num2
            print(f"Result: {result}")

    else:
        print("Invalid operator. Please choose +, -, *, or /.")

    again = input("Do another calculation? (yes/no): ")
    
    if again.lower() != "yes":
        print("Goodbye!")
        break