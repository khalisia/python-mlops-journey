limit = int(input("Generate squares up to: "))

squares = [number ** 2 for number in range(1, limit+1)]

print(squares)