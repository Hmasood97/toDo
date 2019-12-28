import Tkinter
import tkMessageBox
import random

#Creating root window
root = Tkinter.Tk()

#Setting title
root.title("Hisham's List")

#root window size
root.geometry("350x300")
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
  makeSure = tkMessageBox.askyesno("are you sure?", "ARE YOU SURE")
  if makeSure == True:
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

def number_tasks():
    num = len(tasks)
    
    message = "number of tasks: %s" %num
    lbl_display["text"]= message









#title
lbl_title = Tkinter.Label(root, text= "To-Do-List", bg="white" )
lbl_title.grid(row=0, column=0)

#display
lbl_display = Tkinter.Label(root, text ="", bg="white")
lbl_display.grid(row=0, column=1)

#Text input 
txt_input = Tkinter.Entry(root, width=20)
txt_input.grid(row=1, column=1)

#add Task button
btn_add_task = Tkinter.Button(root, text = "Add Task", fg = "green", bg= "white", command = add_task)
btn_add_task.grid(row=1, column=0)

#Del button
btn_del = Tkinter.Button(root, text = "Delete Task", fg = "green", bg= "white", command = del_task)
btn_del.grid(row=2, column=0)

btn_delAll = Tkinter.Button(root, text = "Delete All tasks", fg = "green", bg= "white", command = del_all)
btn_delAll.grid(row=3, column=0)


#Sort button ascending
btn_sortA = Tkinter.Button(root, text = "Sort Ascending", fg = "green", bg= "white", command = sortA_task)
btn_sortA.grid(row=4, column=0)

#Sort Descending
btn_sortD = Tkinter.Button(root, text = "Sort Descending", fg = "green", bg= "white", command = sortD_task)
btn_sortD.grid(row=5, column=0)

btn_numberTasks = Tkinter.Button(root, text = "Number of Tasks", fg = "green", bg= "white", command = number_tasks)
btn_numberTasks.grid(row=6, column=0)

btn_exit = Tkinter.Button(root, text = "Exit", fg = "green", bg= "white", command = exit_task)
btn_exit.grid(row=7, column=0)


listbox_tasks = Tkinter.Listbox(root)
listbox_tasks.grid(row=2, column=1, rowspan=7)




#runs it

root.mainloop()
