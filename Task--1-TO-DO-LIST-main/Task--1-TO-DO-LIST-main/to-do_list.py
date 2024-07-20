# to-do_list

def add_task(tasks, new_task):
    tasks.append({"task": new_task, "completed": False})

def display_tasks(tasks):
    print("\n--- To-Do List ---")
    for i, task in enumerate(tasks, start=1):
        status = "✓" if task["completed"] else " "
        print(f"{i}. [{status}] {task['task']}")
    print("------------------")

def mark_completed(tasks, task_number):
    if 1 <= task_number <= len(tasks):
        tasks[task_number - 1]["completed"] = True
        print(f"Task {task_number} marked as completed.")
    else:
        print("Invalid task number. Please try again.")

def main():
    tasks = []
    while True:
        print("\n1. Add Task")
        print("2. Display Tasks")
        print("3. Mark Task as Completed")
        print("4. Exit")
        choice = input("Enter your choice (1/2/3/4): ")

        if choice == "1":
            new_task = input("Enter the task: ")
            add_task(tasks, new_task)
        elif choice == "2":
            display_tasks(tasks)
        elif choice == "3":
            task_number = int(input("Enter the task number to mark as completed: "))
            mark_completed(tasks, task_number)
        elif choice == "4":
            print("Exiting the To-Do List App. Have a great day!")
            break
        else:
            print("Invalid choice. Please select a valid option.")

if __name__ == "__main__":
    main()