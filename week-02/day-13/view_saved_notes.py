print("1. Add Note")
print("2. View Notes")

choice = input("Choose an option: ")

if choice == "1":

    note=input(" write a note: ")

    with open("notes.txt", "a") as file:
        file.write(note + "\n")

    print("Note saved fully.")

elif choice == "2":

    try:
        with open("notes.txt", "r") as file:
            print("\nYour Notes:")
            print(file.read())

    except FileNotFoundError:
        print("No notes found.")