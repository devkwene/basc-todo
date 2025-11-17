import os
from datetime import datetime

TASKS_FILE = "tasks.txt"

def load_tasks():
    if not os.path.exists(TASKS_FILE):
        return []
    tasks = []
    with open(TASKS_FILE, "r") as file:
        for line in file:
            parts = line.strip().split(" | ")
            if len(parts) == 5:
                task, category, priority, due_date, status = parts
                tasks.append({
                    "task": task,
                    "category": category,
                    "priority": priority,
                    "due_date": due_date,
                    "status": status
                })
    return tasks

def save_tasks(tasks):
    with open(TASKS_FILE, "w") as file:
        for t in tasks:
            file.write(f"{t['task']} | {t['category']} | {t['priority']} | {t['due_date']} | {t['status']}\n")

def display_tasks(tasks):
    if not tasks:
        print("\nNo tasks yet. Add one!\n")
        return
    print("\nYour Tasks:")
    print("-----------------------------------------------------------")
    for i, t in enumerate(tasks, 1):
        print(f"{i}. {t['task']} | {t['category']} | {t['priority']} | Due: {t['due_date']} | Status: {t['status']}")
    print("-----------------------------------------------------------\n")

def add_task(tasks):
    task = input("Task description: ").strip()
    category = input("Category (Work/Personal/Other): ").strip()
    priority = input("Priority (Low/Medium/High): ").strip()
    due_date = input("Due date (YYYY-MM-DD): ").strip()
    status = "Pending"

    tasks.append({
        "task": task,
        "category": category,
        "priority": priority,
        "due_date": due_date,
        "status": status
    })
    save_tasks(tasks)
    print("\nTask added!\n")

def delete_task(tasks):
    display_tasks(tasks)
    try:
        num = int(input("Enter task number to delete: "))
        if 1 <= num <= len(tasks):
            removed = tasks.pop(num - 1)
            save_tasks(tasks)
            print(f"\nDeleted: {removed['task']}\n")
        else:
            print("\nInvalid task number!\n")
    except ValueError:
        print("\nEnter a valid number.\n")

def mark_completed(tasks):
    display_tasks(tasks)
    try:
        num = int(input("Enter task number to mark as completed: "))
        if 1 <= num <= len(tasks):
            tasks[num - 1]["status"] = "Completed"
            save_tasks(tasks)
            print("\nTask marked as completed!\n")
        else:
            print("\nInvalid task number!\n")
    except ValueError:
        print("\nEnter a valid number.\n")

def edit_task(tasks):
    display_tasks(tasks)
    try:
        num = int(input("Enter task number to edit: "))
        if 1 <= num <= len(tasks):
            t = tasks[num - 1]
            print("\nLeave field blank to keep current value.\n")

            new_task = input(f"New task description ({t['task']}): ").strip()
            new_category = input(f"New category ({t['category']}): ").strip()
            new_priority = input(f"New priority ({t['priority']}): ").strip()
            new_due_date = input(f"New due date ({t['due_date']}): ").strip()

            if new_task: t['task'] = new_task
            if new_category: t['category'] = new_category
            if new_priority: t['priority'] = new_priority
            if new_due_date: t['due_date'] = new_due_date

            save_tasks(tasks)
            print("\nTask updated!\n")
        else:
            print("\nInvalid task number!\n")
    except ValueError:
        print("\nEnter a valid number.\n")

def search_tasks(tasks):
    keyword = input("Enter keyword to search: ").strip().lower()
    results = [t for t in tasks if keyword in t['task'].lower()]

    if not results:
        print("\nNo matching tasks found.\n")
        return

    print("\nSearch Results:")
    print("-----------------------------------------------------------")
    for i, t in enumerate(results, 1):
        print(f"{i}. {t['task']} | {t['category']} | {t['priority']} | Due: {t['due_date']} | Status: {t['status']}")
    print("-----------------------------------------------------------\n")

def main():
    tasks = load_tasks()

    while True:
        print("Advanced To-Do List App")
        print("-------------------------")
        print("1. Add a task")
        print("2. View tasks")
        print("3. Delete a task")
        print("4. Mark task as completed")
        print("5. Edit a task")
        print("6. Search tasks")
        print("7. Exit")

        choice = input("\nEnter choice (1–7): ")

        if choice == "1":
            add_task(tasks)
        elif choice == "2":
            display_tasks(tasks)
        elif choice == "3":
            delete_task(tasks)
        elif choice == "4":
            mark_completed(tasks)
        elif choice == "5":
            edit_task(tasks)
        elif choice == "6":
            search_tasks(tasks)
        elif choice == "7":
            print("Goodbye!")
            break
        else:
            print("\nInvalid choice. Try again.\n")

if __name__ == "__main__":
    main()
