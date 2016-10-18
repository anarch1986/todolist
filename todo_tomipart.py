todolist=open("todolist.txt","a")
todolist.close()
szam=0

def listing():
    todolist=open("todolist.txt","r")
    print("You saved the following to-do items:")
    content=todolist.read()
    print(content)
    todolist.close()

def adding():
    todolist=open("todolist.txt","a")
    add_item=input("Add an item: ")
    todolist.write(str(szam+1)+".[ ] "+(add_item))
    todolist.close()



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
    #
    #
    #text_file=open("todolist.txt")
    #text_file.write