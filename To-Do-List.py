# Function to display the menu
def display_menu():
    print("\nTo-Do List App")
    print("1. Add a Task")
    print("2. View All Tasks")
    print("3. Delete a Task")
    print("4. Exit")

# Function to load tasks from the file
def load_tasks(filename):
    try:
        with open(filename, 'r') as file:
            tasks = file.readlines()
            tasks = [task.strip() for task in tasks]  # Remove newline characters
        return tasks
    except FileNotFoundError:
        return []

# Function to save tasks to the file
def save_tasks(filename, tasks):
    with open(filename, 'w') as file:
        for task in tasks:
            file.write(task + '\n')

# Function to add a task
def add_task(tasks):
    task = input("Enter the new task: ")
    tasks.append(task)
    print(f"Task '{task}' added.")

# Function to view all tasks
def view_tasks(tasks):
    if not tasks:
        print("No tasks available.")
    else:
        print("\nYour To-Do List:")
        for index, task in enumerate(tasks, start=1):
            print(f"{index}. {task}")

# Function to delete a task
def delete_task(tasks):
    view_tasks(tasks)
    if tasks:
        try:
            task_num = int(input("Enter the number of the task to delete: "))
            if 1 <= task_num <= len(tasks):
                removed_task = tasks.pop(task_num - 1)
                print(f"Task '{removed_task}' deleted.")
            else:
                print("Invalid task number.")
        except ValueError:
            print("Please enter a valid number.")

# Main function to run the to-do list app
def to_do_list_app():
    filename = "tasks.txt"
    tasks = load_tasks(filename)
    
    while True:
        display_menu()
        choice = input("Enter your choice: ")
        
        if choice == '1':
            add_task(tasks)
        elif choice == '2':
            view_tasks(tasks)
        elif choice == '3':
            delete_task(tasks)
        elif choice == '4':
            save_tasks(filename, tasks)
            print("Tasks saved. Exiting the app. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

# Run the to-do list app
if __name__ == "__main__":
    to_do_list_app()
