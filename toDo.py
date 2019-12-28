import Tkinter

import random

#Creating root window
root = Tkinter.Tk()

# Function Definitions

def add_task():
    pass








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
btn_add_task = Tkinter.Button(root, text = "Add Task", fg = "green", bg= "white")
btn_add_task.pack()

#Del button
btn_del = Tkinter.Button(root, text = "Delete Task", fg = "green", bg= "white")
btn_del.pack()


#Sort button ascending
btn_sortA = Tkinter.Button(root, text = "Sort Ascending", fg = "green", bg= "white")
btn_sortA.pack()

#Sort Descending
btn_sortD = Tkinter.Button(root, text = "Sort Descending", fg = "green", bg= "white")
btn_sortD.pack()




#runs it

root.mainloop()
