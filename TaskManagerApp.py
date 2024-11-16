
def welcome_message():
    print("Hello Greeting ! Hope you're doing great.")
    print("Welcome to the Task manager !!")

def display_menu():
    print("Chose any features from below : ")
    print("1. Add task")
    print("2. View tasks")
    print("3. Delete task")
    print("4. quite")

def add_task() :
    global tasks_database

    task_details = input("Enter the task :").lower()

    if len(task_details.strip()) >=1 :
        tasks_database.append(task_details)
        print("Success. Task has been added.")
    else:
        print("ERROR: Task cannot be empty")

def view_tasks() :

    print("Following  are the tasks in the database :")

    if len(tasks_database) >= 1 :
        for pos , task_data in enumerate(tasks_database) :
            print(pos+1 , task_data)
    else:
        print("ERROR: No tasks are available to display. Database is empty. Please add some.")

def delete_tasks() :
    if len(tasks_database) >= 1:
        view_tasks()
        task_number = int(input("Enter the task number you want to delete :"))
        if 1 <= task_number <= len(tasks_database) :
                removedTask = tasks_database.pop(task_number-1)

                print("The task :" ,removedTask , " has been removed. Successfully." )
        else:
                print("ERROR: The task number you entered is Invalid")
    else:
        print("ERROR: No tasks available to delete.")


tasks_database = []

welcome_message()

while True :
    display_menu()
    try:
        choice = int(input("Enter the choice from above menu :"))

        if choice == 1 :
            add_task()
        elif choice == 2:
            view_tasks()
        elif choice == 3:
            delete_tasks()
        elif choice == 4:
            print("Exiting the task manager. Thank you for using the application. Good bye.")
            break
        else:
            print("Invalid choice. Please enter a valid preference.")
    except Exception as error :
        print("Error occurred : " , error)
    finally:
        print("Returning to main menu...")
        print("\n_____________________________________\n")
