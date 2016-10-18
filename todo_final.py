# Welcome to team DEPT-H's To-do app!

# We run this script to be sure if this .txt file exists.
# If exist's it opens.
# If it does not exist it creats.

todolist = open("todolist.txt", "a")
todolist.close()

# Here we create a list which handles our To-do's with the .txt file and definitions.

todolist = open("todolist.txt", "r")
tasks = todolist.readlines()
todolist.close()


# We defined the necessary commands and visual elements to operate this app.

def print_task():
    for n in range(len(tasks)):
        print(n+1, '. ', tasks[n], sep='', end='')


def listing():
    print("You saved the following to-do items:")
    print_task()


def adding():
    add_item = input("Add an item: ")
    tasks.append("[ ] "+add_item+"\n")
    print("Item added.")
    

def marking():
    print("You saved the following to-do items:")
    print_task()
    marktask = input("Which one you want to mark as completed: ")
    b = int(marktask)-1

    print(tasks[b][4:-1] + " is completed")
    
    tasks[b] = "[x]" + tasks[b][3:]
        

def archive():
    global tasks 
    task_ghost = []
    for task in tasks:
        if "[x]" not in task:
            task_ghost.append(task)
    tasks = task_ghost  
    print("All completed tasks got deleted.")

# This one is the main function. It collects the parts of the script.


def main_function():
    while True is True:
        ask = input("Please specifiy a command [list, add, mark, archive]: ")
        if ask == "list":
            listing()
            print()
        elif ask == "add":
            adding()
            print()
        elif ask == "mark":
            marking()
            print()    
        elif ask == "archive":
            archive()
            print()
        else:
            todolist_open = open("todolist.txt", "w")
            for i in tasks:
                todolist_open.write(i)
            print("Goodbye!")
            exit()
        
# We execute the program here.
     
main_function()
