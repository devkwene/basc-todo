import os

TASKS_FILE = "tasks.txt"

def load_tasks():
    if not os.path.exists(TASKS_FILE):
        return []
    with open(TASKS_FILE, "r") as file:
        return [task.strip() for task in file.readlines()]

def save_tasks(tasks):
    with open(TASKS_FILE, "w") as file:
        file.writelines([task + "\n" for task in tasks])

def display_tasks(tasks):
    if not tasks:
        print("\nNo tasks yet. Add one!\n")
        return
    print("\nYour Tasks:")
    print("-----------------")
    for i, task in enumerate(tasks, 1):
        print(f"{i}. {task}")
    print()

def main():
    tasks = load_tasks()

    while True:
        print("To-Do List App")
        print("---------------")
        print("1. Add a task")
        print("2. View tasks")
        print("3. Delete a task")
        print("4. Exit")

        choice = input("\nEnter choice (1-4): ")

        if choice == "1":
            task = input("Enter task: ").strip()
            if task:
                tasks.append(task)
                save_tasks(tasks)
                print("Task added!\n")

        elif choice == "2":
            display_tasks(tasks)

        elif choice == "3":
            display_tasks(tasks)
            try:
                num = int(input("Enter task number to delete: "))
                if 1 <= num <= len(tasks):
                    removed = tasks.pop(num - 1)
                    save_tasks(tasks)
                    print(f"Deleted: {removed}\n")
                else:
                    print("Invalid task number!\n")
            except ValueError:
                print("Enter a valid number.\n")

        elif choice == "4":
            print("Goodbye!")
            break

        else:
            print("Invalid choice. Try again.\n")

if __name__ == "__main__":
    main()
