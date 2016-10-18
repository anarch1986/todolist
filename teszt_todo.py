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
    add_item=input("Add an item: ")
    tasks.append("[ ] "+add_item+"\n")
    print("Item added")
    

def marking():
    todolist=open("todolist.txt","r")
    print("You saved the following to-do items:")
    content=todolist.read()
    print(content)
    marktask=input("Which one you want to mark as completed: ")





while 1==1:
    ask=input("Please specifiy a command [list, add, mark,archive]: ")
    if ask==("list"):
        listing()
    elif ask==("add"):
        adding()
    elif ask==("mark"):
        print("ok")
    elif ask==("archive"):
        print("ok")
    else:
        print("Goodbye!")
        break


    #
    #fgjfd
    #
    #text_file=open("todolist.txt")
    #text_file.write