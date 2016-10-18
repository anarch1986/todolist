todolist=open("todolist.txt","a")
todolist.close()

todolist=open("todolist.txt","r")
tasks=todolist.readlines()

def listing():
    print("You saved the following to-do items:")
    for n in range(len(tasks)):
        print(n+1, '.', tasks[n], sep='', end='')
    todolist.close()

def adding():
    todolist=open("todolist.txt","a")
    add_item=input("Add an item: ")
    todolist.write("[ ] "+(add_item)+"\n")
    todolist.close()

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






ask=input("Please specifiy a command [list, add, mark,archive]: ")
if ask==("list"):
    listing()
elif ask==("add"):
    adding()
elif ask==("mark"):
    marking()
elif ask==("archive"):
    print("ok")
else:
    exit()


    #
    #fgjfd
    #
    #text_file=open("todolist.txt")
    #text_file.write
