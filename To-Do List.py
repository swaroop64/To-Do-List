#To-Do List
tasks = []

def addTask():
    task = input("Please enter a task:")
    tasks.append(task)
    print(f"{task} has been added to your list.")

def listTasks():
    if not tasks:
        print("There are no tasks currently")
    else:
        print('Current Tasks:')
        for index, task in enumerate(tasks):
            print(f"Task #{index}. {task}")
   
def deleteTask():
    listTasks()
    try:
        taskToDelete = int(input("Enter the number of the task you want to delete:"))
        if taskToDelete >=0 and taskToDelete < len(tasks):
            tasks.pop(taskToDelete)
            print(f"Task {taskToDelete} has been removed.")
        else:
            print(f"Task {taskToDelete} was not found")
    except:
        print("Invalid Input")

if __name__=="__main__":
    #creating a loop to run the app
    print("Welcome to the TO_DO List App:")
    while True:
        print('\n')
        print('Please select one of the following options:\n')
        print("---------------------------------------------")
        print('1. Add a new Task')
        print('2. Delete a Task')
        print('3. List Task')
        print('4. Quit')

        choice = input("Enter your choice: ")

        if(choice == '1'):
            addTask()
        elif(choice == '2'):
            deleteTask()
        elif(choice == '3'):
            listTasks()
        elif(choice == '4'):
            break
        else:
            print('Invalid Input.\n Please Try Again')

    print("GoodBye 👋👋")