import Tkinter

import random

#Creating root window
root = Tkinter.Tk()

#Setting title
root.title("Hisham's List")

#root window size
root.geometry("220x500")
# Function Definitions

#creating a list to hold all of the tasks

tasks = []
tasks = []

def update_listbox():
    clear_listbox()
    for task in tasks:
        listbox_tasks.insert("end", task)

def clear_listbox():
    listbox_tasks.delete(0, "end")

def add_task():
    task = txt_input.get()
    if task != "":
        tasks.append(task)
        update_listbox()
    else:
        lbl_display["text"]= "Enter a task"


def del_task():
    task = listbox_tasks.get("active")
    if task in tasks:
        tasks.remove(task)
        update_listbox()

def del_all():
  global tasks
  tasks = []
  update_listbox()

def sortA_task():
    tasks.sort()
    update_listbox()

def sortD_task():
    tasks.sort()
    tasks.reverse()
    update_listbox()

def exit_task():
    pass

def number_Tasks():
    num = len(tasks)
    
    message = "number of tasks: %s" %num
    lbl_display["text"]= message









#title
lbl_title = Tkinter.Label(root, text= "To-Do-List", bg="white" )
lbl_title.pack()

#display
lbl_display = Tkinter.Label(root, text ="", bg="white")
lbl_display.pack()

#Text input 
txt_input = Tkinter.Entry(root, width=15)
txt_input.pack()

#add Task button
btn_add_task = Tkinter.Button(root, text = "Add Task", fg = "green", bg= "white", command = add_task)
btn_add_task.pack()

#Del button
btn_del = Tkinter.Button(root, text = "Delete Task", fg = "green", bg= "white", command = del_task)
btn_del.pack()

btn_delAll = Tkinter.Button(root, text = "Delete All tasks", fg = "green", bg= "white", command = del_all)
btn_delAll.pack()


#Sort button ascending
btn_sortA = Tkinter.Button(root, text = "Sort Ascending", fg = "green", bg= "white", command = sortA_task)
btn_sortA.pack()

#Sort Descending
btn_sortD = Tkinter.Button(root, text = "Sort Descending", fg = "green", bg= "white", command = sortD_task)
btn_sortD.pack()



btn_exit = Tkinter.Button(root, text = "Exit", fg = "green", bg= "white", command = exit_task)
btn_exit.pack()


listbox_tasks = Tkinter.Listbox(root)
listbox_tasks.pack()




#runs it

root.mainloop()
