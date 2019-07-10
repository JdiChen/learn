from tkinter import *

root = Tk()

v = IntVar()
def show():
    print( sb.get())
sb = Spinbox(root,
        text = "kdk",
        from_ = 0,
        to = 10,
        increment = 2,
        state = "readonly",
             textvariable = v,
             command = show).pack()


Label(root,textvariable = sb.get()).pack()
root.mainloop()
