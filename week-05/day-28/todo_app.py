import json
from pathlib import Path

TASKS_FILE = "tasks.json"

def load_tasks():
    """Load tasks from the JSON file."""
    if Path(TASKS_FILE).exists():
        try:
            with open(TASKS_FILE, "r") as file:
                return json.load(file)
        except json.JSONDecodeError:
            return []
    return[]

def save_tasks(tasks):
    """Save tasks to the JSON file."""
    with open(TASKS_FILE, "w")as file:
        json.dump(tasks, file, indent=4)

def view_tasks(tasks):
    """Display all tasks."""
    if not tasks:
        print("\nNo tasks are available.")
        return
    
    print("\nTo-Do list")
    print("-" * 30) 

    for index, task in enumerate(tasks, start = 1):
        print(f"{index}.{task}")

def add_task(tasks):
    """Add a new task."""
    task = input("Enter a new task: ").strip()

    if task:
        tasks.append(task)
        save_tasks(tasks)
        print("Task added successfully!")
    else:
        print("Task cannot be empty.")
              
def delete_task(tasks):
    """Delete a task."""
    view_tasks(tasks)

    if not tasks:
        return

    try:
        choice = int(input("\nEnter task number to delete: "))

        if 1 <= choice <= len(tasks):
            removed = tasks.pop(choice - 1)
            save_tasks(tasks)
            print(f'"{removed}" deleted.')
        else:
            print("Invalid task number.")
    
    except ValueError:
        print("Please enter a valid number.")

def main():
    tasks = load_tasks()

    while True:
        print("/n ======TO DO APP ======")
        print("1. View Tasks")
        print("2. Add Task")
        print("3. Delete Task")
        print("4. Exit")

        choice = input("Please enter a choice: ")

        if choice == "1":
            view_tasks(tasks)
        elif choice == "2":
            add_task(tasks)
        elif choice == "3":
            delete_task(tasks)
        elif choice == "4":
            print("Goodbye!")
            break
                
        else:
            print("Invalid option")

if __name__ =="__main__":
        main()
                

    
    






