try:
    number = int(input("Enter a number: "))
except ValueError:
    print("Please enter a valid integer.")
else:
    if number % 2 == 0:
        print(f"{number} is even.")
    else:
        print(f"{number} is odd.")