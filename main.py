my_tasks = []


def add_task():
    task = input("Enter a task: ")
    my_tasks.append(task)
    print(f"Task added: {task}\n")


def view_tasks():
    print("\n--- To-Do List ---")
    for index, task in enumerate(my_tasks):
        print(index, task)
    print("------------------\n")


def main():
    while True:
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Exit")
        choice = input("Choose an option (1/2/3): ")

        if choice == "1":
            add_task()
        elif choice == "2":
            view_tasks()
        elif choice == "3":
            print("Program ended.")
            break
        else:
            print("Invalid choice, try again.\n")


if __name__ == "__main__":
    main()
