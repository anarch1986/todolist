todolist=open("todolist.txt","a")
todolist.close()

def listing():
    todolist=open("todolist.txt","r")
    print("You saved the following to-do items:")
    content=todolist.read()
    print(content)
    todolist.close()

def adding():
    todolist=open("todolist.txt","a")
    add_item=input("Add an item: ")
    todolist.write(".[ ] "+(add_item)+"\n")
    todolist.close()

def marking():
    todolist=open("todolist.txt","r")
    print("You saved the following to-do items:")
    content=todolist.read()
    print(content)
    marktask=input("Which one you want to mark as completed: ")




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
    exit()


    #
    #fgj
    #
    #text_file=open("todolist.txt")
    #text_file.write
