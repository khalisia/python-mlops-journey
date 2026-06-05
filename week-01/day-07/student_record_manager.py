students = {}

while True:
    print("\n=== STUDENT RECORD MANAGER ===")
    print("1. Add Student") 
    print("2. View Student") 
    print("3. View All Students") 
    print("4. Exit") 
    print("5. Delete Student")

    choise = input("Choose an option : ")

    if choise == "1":
        name = input("Enter student name: ")
        grade = input("Enter student grade: ")
        age = input("Enter student age: ")
        
        students[name] = {"grade": grade, "age": age}

        print("Student added successfully.")

    elif choise == "2":
        name = input("Enter student name to view: ")

        grade = students.get(name)

        if grade:
            print(f"{name}: {grade}")
        else:
            print("Student not found.")

    elif choise =="3":
        print("\nStudent Records:")

        if len(students) == 0:
            print("No student records found.")
        else:
            for name, grade in students.items():
                print(f"{name}: {grade}")
                
    elif choise == "4":
        print("Exiting. Goodbye!")
        break

    elif choise == "5":
        name = input("Enter student name to delete: ")

        if name in students:
            del students[name]
            print("Student deleted successfully.")
        else:
            print("Student not found.")
    