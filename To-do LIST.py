class TodoList:
    def __init__(self):
        self.tasks = {}

    def add_task(self, task_id, task_desc):
        """Add a new task with a unique task ID and description."""
        self.tasks[task_id] = {"Description": task_desc, "Completed": False}
        print(f"Task '{task_desc}' added with ID: {task_id}.")

    def update_task(self, task_id, new_desc=None, completed=None):
        """Update a task's description or mark it as completed."""
        if task_id in self.tasks:
            if new_desc:
                self.tasks[task_id]["Description"] = new_desc
            if completed is not None:
                self.tasks[task_id]["Completed"] = completed
            print(f"Task {task_id} updated.")
        else:
            print("Task ID not found.")

    def delete_task(self, task_id):
        """Delete a task by ID."""
        if task_id in self.tasks:
            del self.tasks[task_id]
            print(f"Task {task_id} deleted.")
        else:
            print("Task ID not found.")

    def show_tasks(self):
        """Display all tasks with their completion status."""
        if not self.tasks:
            print("No tasks to show.")
            return
        for task_id, details in self.tasks.items():
            status = "Completed" if details["Completed"] else "Pending"
            print(f"[{task_id}] {details['Description']} - {status}")


def main():
    todo_list = TodoList()

    while True:
        print("\n--- To-Do List ---")
        print("1. Add Task")
        print("2. Update Task")
        print("3. Delete Task")
        print("4. Show Tasks")
        print("5. Exit")
        choice = input("Choose an option (1-5): ")

        if choice == '1':
            task_id = input("Enter Task ID: ")
            task_desc = input("Enter Task Description: ")
            todo_list.add_task(task_id, task_desc)

        elif choice == '2':
            task_id = input("Enter Task ID to update: ")
            new_desc = input("Enter new description (or leave blank): ")
            status = input("Mark as completed? (y/n): ").strip().lower()
            completed = True if status == 'y' else False if status == 'n' else None
            todo_list.update_task(task_id, new_desc if new_desc else None, completed)

        elif choice == '3':
            task_id = input("Enter Task ID to delete: ")
            todo_list.delete_task(task_id)

        elif choice == '4':
            todo_list.show_tasks()

        elif choice == '5':
            print("Exiting To-Do List application.")
            break

        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()

