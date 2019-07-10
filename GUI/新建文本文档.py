from tkinter import *

root  = Tk()
v = IntVar()
def show():
    win = Tk()

    Label(win,bg = "white",text = str(v.get())).pack()
    
#for i in range(5):
    
bt = Checkbutton(root,text = "455",
                variable = v,
                )

Button(root,text="text",command = show).pack()
bt.pack()

mainloop()
