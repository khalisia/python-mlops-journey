items = input("Enter items separated by spaces: ").split()

unique_items = []

for item in items:
    if item not in unique_items:
        unique_items.append(item)

print("\nWithout Duplicates:")
print(unique_items)
