shopping_list =[]

while True:
    print("\n--- SHOPPING lIST MENU ---")
    print("1. View list")
    print("2. Add item")
    print("3. Remove item")
    print("4. Exit")

    choice = input("Choose an option: ")

    if choice == "1":
        print("\nShopping List:")
        
        if len(shopping_list) == 0:
            print("List is empty.")
        else:
            for item in shopping_list:
                print(f"- {item}")

    elif choice == "2":
        item = input("Enter the item to add: ")
        shopping_list.append(item)
        print(f"{item} added to the list.")

    elif choice == "3":
        item = input("Enter item to remove: ")
        
        if item in shopping_list:
            shopping_list.remove(item)
            print(f"{item} removed from the list.")
        else:
            print(f"{Item} not found.")
    elif choice == "4":
        print("Goodbye!")
        break
    else:
        print("Invalid option.")

