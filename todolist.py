def task():
    tasks = []
    print("-----> WELCOME TO THE TASK MANAGEMENT APP <----")

    total_task = int(input("Enter how many tasks you want to add = "))
    for i in range(1, total_task+1 ):
        task_name = input(f"Enter task {i} = ")
        tasks.append(task_name)
    print(f"Today's tasks are:\n{tasks}")

    while True:
        try:
            print("enter your operation which you want:")
            print("1.Add")
            print("2.Update")
            print("3.Delete")
            print("4.View")
            print("5.Exit")
            operation = int(input("enter your choice(1-5):"))
            
            if operation == 1:
                add = input("Enter task you want to add = ")
                tasks.append(add)
                print(f"Task '{add}' has been successfully added.")

            elif operation == 2:
                updated_val = input("Enter the task name you want to update = ")
                if updated_val in tasks:
                    up = input("Enter new task = ")
                    ind = tasks.index(updated_val)
                    tasks[ind] = up
                    print(f"Updated task '{updated_val}' to '{up}'.")

                else:
                    print("Task not found.")

            elif operation == 3:
                delete_val = input("Which task you want to delete = ")
                if delete_val in tasks:
                    tasks.remove(delete_val)
                    print(f"Task '{delete_val}' has been deleted.")
                else:
                    print("Task not found.")

            elif operation == 4:
                print(f"Total tasks: {tasks}")

            elif operation == 5:
                print("Thank you...")
                break

            else:
                print("Invalid input. Please enter a number from 1 to 5.")
        except ValueError:
            print("Invalid input. Please enter a valid number.")


task()
