
def load_tasks():
    try:
        with open("sandbox/tasks.txt", "r") as file:
            tasks = file.read().splitlines()
    except FileNotFoundError:
        return []
    return tasks

def save_tasks(tasks):
    with open("sandbox/tasks.txt", "w") as file:
        for task in tasks:
            file.write(task + "\n")

def add_task(tasks):
    task_to_append = input("Enter a task: ")
    tasks.append(task_to_append)
    save_tasks(tasks)

def view_tasks(tasks):
    for task in tasks:
        print(task)

def remove_tasks(tasks):
    try:
        task_to_remove = input("Enter the task to remove: ")
        tasks.remove(task_to_remove)
        save_tasks(tasks)
    except ValueError:
        print("The task does not exist")


tasks = load_tasks()
user_input = 0
while user_input != 4:
    print("Menu:")
    print("1. Add a task")
    print("2. View tasks")
    print("3. Remove a task")
    print("4. Quit")
    try:
        user_input = int(input("Enter your option: "))
    except ValueError:
        print("Please enter a valid number")
        continue
    if user_input > 4 or user_input < 1:
        print("Invalid choice")
    elif user_input == 1:
        add_task(tasks)
    elif user_input == 2:
        view_tasks(tasks)
    elif user_input == 3:
        remove_tasks(tasks)




