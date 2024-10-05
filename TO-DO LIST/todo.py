# To-Do List Application

# Initialize an empty to-do list
todo_list = []

# Function to display the to-do list
def display_tasks():
    if len(todo_list) == 0:
        print("\nYour to-do list is empty.")
    else:
        print("\nYour To-Do List:")
        for index, task in enumerate(todo_list, start=1):
            print(f"{index}. {task}")
    print()

# Function to add a new task
def add_task():
    task = input("Enter the task you want to add: ")
    todo_list.append(task)
    print(f'"{task}" has been added to your to-do list.')

# Function to update a task
def update_task():
    display_tasks()
    if len(todo_list) > 0:
        task_number = int(input("Enter the number of the task you want to update: "))
        if 1 <= task_number <= len(todo_list):
            new_task = input("Enter the updated task: ")
            todo_list[task_number - 1] = new_task
            print(f"Task {task_number} has been updated to: {new_task}")
        else:
            print("Invalid task number.")
    else:
        print("No tasks available to update.")

# Function to remove a task
def remove_task():
    display_tasks()
    if len(todo_list) > 0:
        task_number = int(input("Enter the number of the task you want to remove: "))
        if 1 <= task_number <= len(todo_list):
            removed_task = todo_list.pop(task_number - 1)
            print(f'"{removed_task}" has been removed from your to-do list.')
        else:
            print("Invalid task number.")
    else:
        print("No tasks available to remove.")

# Function to manage the to-do list
def todo_app():
    while True:
        print("\nTo-Do List Options:")
        print("1. View To-Do List")
        print("2. Add a Task")
        print("3. Update a Task")
        print("4. Remove a Task")
        print("5. Exit")
        
        choice = input("Enter your choice (1-5): ")
        
        if choice == '1':
            display_tasks()
        elif choice == '2':
            add_task()
        elif choice == '3':
            update_task()
        elif choice == '4':
            remove_task()
        elif choice == '5':
            print("Exiting the To-Do List application. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

# Run the to-do list application
todo_app()
