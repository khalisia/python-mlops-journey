import csv 
with open("students.csv","r") as file:
    reader = csv.DictReader(file)

    print("Student Records\n")

    for row in reader:
        print(f"Name: {row['Name']}")
        print(f"Age: {row['Age']}")
        print(f"Course: {row['Course']}")
        print("-"* 20)