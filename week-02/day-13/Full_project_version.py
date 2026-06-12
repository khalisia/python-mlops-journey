while True:
    print("\n===Notes App===")
    print("1. Add Note")
    print("2. View Notes")
    print("3. Exit")
    print("4. Count Notes")
    print("5. Save Timestamp")
    print("6, Clear Notes")

    choice = input("Enter your choice: ")

    if choice == "1":

        note = input("Enter note: ")

        with open("notes.txt", "a") as file:
            file.write(note + "\n")

        print("Note added successfully!")

    elif choice == "2":
        try:
            with open("notes.txt", "r") as file:
                print("\nSaved Notes:")
                print(file.read())

        except FileNotFoundError:
            print("No notes saved yet.")

    elif choice == "3":
        print("Exiting the app. Goodbye!")
    
    elif choice == "4":
        try:
            with open("notes.txt", "r") as file:
                notes = file.readlines()
                
                print(f"Total number of notes: {len(notes)}")

        except FileNotFoundError:
            print("No notes saved yet.")

    elif choice == "5":
        from datetime import datetime

        timestamp = datetime.now()

        with open("notes.txt", "a") as file:
            file.write(f"{timestamp} - {note}\n")
    
    elif choice == "6":
        with open("notes.txt", "w") as file:
            pass

        print("All notes cleared successfully!")

