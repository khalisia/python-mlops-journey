try:
    num1 = float(input("Enter a number: "))
    num2 = float(input("Enter the second number: "))

    result = num1/num2

except ValueError:
    print("Please enter a number.")
except ZeroDivisionError:
    print("You cannot divide by zero")
else:
    print(f"Result: {result}")
finally:
    print("Calculator closed.")