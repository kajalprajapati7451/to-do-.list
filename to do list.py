def main():
    tasks = []

    while True:
        print("\n****** TO-DO LIST *****")
        print("1. Add Task")
        print("2. Show Tasks")
        print("3. Mark Task as Done")
        print("4. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            print()
            n_tasks = int(input("How many tasks do you want to add? "))

            for i in range(n_tasks):
                task = input(f"Enter task {i + 1}: ")
                tasks.append({"task": task, "done": False})
                print("Task added!")

        elif choice == '2':
            if tasks:
                print("\nTasks:")
                for index, task in enumerate(tasks):
                    status = "Done" if task["done"] else "Not Done"
                    print(f"{index + 1}. {task['task']} - {status}")
            else:
                print("\nNo tasks added yet.")

        elif choice == '3':
            if tasks:
                task_index = int(input("Enter the task number to mark as done: ")) - 1
                if 0 <= task_index < len(tasks):
                    tasks[task_index]["done"] = True
                    print("Task marked as done!")
                else:
                    print("Invalid task number.")
            else:
                print("\nNo tasks available to mark as done.")

        elif choice == '4':
            print("Exiting the To-Do List. Goodbye!")
            break

        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
