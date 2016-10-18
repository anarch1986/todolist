todolist=open("todolist.txt","a")
todolist.close()

todolist=open("todolist.txt","r")
tasks=todolist.readlines()
todolist.close()

def pint_task():
    for n in range(len(tasks)):
        print(n+1, '.', tasks[n], sep='', end='')

def listing():
    print("You saved the following to-do items:")
    pint_task()

def adding():
    add_item=input("Add an item: ")
    tasks.append("[ ] "+add_item+"\n")
    print("Item added")
    
def marking():
    print("You saved the following to-do items:")
    pint_task()
    marktask=input("Which one you want to mark as completed: ")
    
    b = int(marktask)-1
    
    tasks[b] = "[x]" + tasks[b][3:]
    pint_task()
        

def archive():
    global tasks 
    task_ghost=[]
    for task in tasks:
        if not "[x]" in task:
            task_ghost.append(task)
    tasks = task_ghost  

while 1==1:
    ask=input("Please specifiy a command [list, add, mark,archive]: ")
    if ask==("list"):
        listing()
    elif ask==("add"):
        adding()
    elif ask==("mark"):
        marking()
    elif ask==("archive"):
        archive()
    else:
        todolist=open("todolist.txt","w")
        todolist.write(str(tasks))
        print("Goodbye!")
        exit()