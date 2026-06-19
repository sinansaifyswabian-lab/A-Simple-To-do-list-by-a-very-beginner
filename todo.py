tasks = []
print("A Simple To-Do list")
# Task Adding Function
def add_tasks():
    task = input("Task: ")
    status = input("Done Or Not : ")
    if status == "Done":
        print('Task Is Done')
    else:
        print("Pending task")

    tasks.append(task)
def remove_tasks():
    task.remove(task)
def show_tasks():
    if len(tasks) == 0:
        print("No Tasks Added Yet!")
    else:
        for task in tasks:
            print("Task :", task)
           
def menu_system():

    while True:
        print("--Your Task Manager--")
        print("1.Add Tasks")
        print("2.Remove Tasks")
        print("3.Show Tasks")
        print("4.Exit")
        choice = int(input("Your Action To Number: "))
        if choice == 1:
            add_tasks()
        elif choice == 2:
            remove_tasks()
        elif choice == 3:
            show_tasks()
        elif choice == 4:
            print("LEAVING TASKS")
            break
        

menu_system()
        

        
    



