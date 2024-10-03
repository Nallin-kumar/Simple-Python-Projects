# Initialize an empty to-do list
todo_list = []

def add_task(task):
    """Add a new task to the to-do list."""
    todo_list.append({"task": task, "completed": False})
    print(f"Task '{task}' added successfully.")

def view_tasks():
    """View all tasks in the to-do list."""
    if not todo_list:
        print("Your to-do list is empty.")
    else:
        print("\nYour to-do list:")
        for idx, item in enumerate(todo_list, start=1):
            status = "Completed" if item["completed"] else "Pending"
            print(f"{idx}. {item['task']} - {status}")

def mark_completed(task_number):
    """Mark a task as completed."""
    if 0 < task_number <= len(todo_list):
        todo_list[task_number - 1]["completed"] = True
        print(f"Task '{todo_list[task_number - 1]['task']}' marked as completed.")
    else:
        print("Invalid task number.")

def delete_task(task_number):
    """Delete a task from the to-do list."""
    if 0 < task_number <= len(todo_list):
        removed_task = todo_list.pop(task_number - 1)
        print(f"Task '{removed_task['task']}' deleted successfully.")
    else:
        print("Invalid task number.")

def main():
    while True:
        print("\nTo-Do List Menu:")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Mark Task as Completed")
        print("4. Delete Task")
        print("5. Exit")

        choice = input("Choose an option (1-5): ")

        if choice == '1':
            task = input("Enter a new task: ")
            add_task(task)
        elif choice == '2':
            view_tasks()
        elif choice == '3':
            task_number = int(input("Enter the task number to mark as completed: "))
            mark_completed(task_number)
        elif choice == '4':
            task_number = int(input("Enter the task number to delete: "))
            delete_task(task_number)
        elif choice == '5':
            print("Exiting the to-do list manager. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

# Run the to-do list manager
main()

