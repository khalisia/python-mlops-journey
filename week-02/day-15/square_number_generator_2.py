while True:
    try: 
        limit = int(input("How many squares?: "))

        squares = [number ** 2 for number in range(1, limit + 1)]

        print("\nSquares:")
        print(squares)

        break
    
    except ValueError:
        print("Please enter a valid whole number.")