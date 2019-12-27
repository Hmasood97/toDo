import Tkinter

import random

#Creating root window
root = Tkinter.Tk()


lbl_title = Tkinter.Label(root, text= "To-Do-List", bg="white" )
lbl_title.pack()


lbl_display = Tkinter.Label(root, text ="", bg="white")
lbl_display.pack()




#runs it

root.mainloop()
