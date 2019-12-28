import Tkinter

import random

#Creating root window
root = Tkinter.Tk()

# Function Definitions
#hay









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



#runs it

root.mainloop()
