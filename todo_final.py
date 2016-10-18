todolist=open("todolist.txt","a")
todolist.close()

todolist=open("todolist.txt","r")
tasks=todolist.readlines()
todolist.close()

def listing():
    print("You saved the following to-do items:")
    for n in range(len(tasks)):
        print(n+1, '.', tasks[n], sep='', end='')

def adding():
    add_item=input("Add an item: ")
    tasks.append("[ ] "+add_item+"\n")
    print("Item added")
    
def marking():
    print("You saved the following to-do items:")
    for a in range(len(tasks)):
        print(a+1, '.', tasks[a], sep='', end='')
    marktask=input("Which one you want to mark as completed: ")
    
    for b in range(len(tasks)):
        if b+1 == int(marktask):
            tasks[b] = "[X]" + tasks[b][3:]
            for n in range(len(tasks)):
                print(n+1, '.', tasks[n], sep='', end='')
        else:
            pass

def archive():
    for task in tasks:
        if "[x]" in task:
            del task

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
    exit()

while 1==1:
    ask=input("Please specifiy a command [list, add, mark,archive]: ")
    if ask==("list"):
        listing()
    elif ask==("add"):
        adding()
    elif ask==("mark"):
        print("ok")
    elif ask==("archive"):
        archive()
    else:
        todolist=open("todolist.txt","w")
        todolist.write(str(tasks))
        print("Goodbye!")
        exit()