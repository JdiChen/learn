from tkinter import *
root = Tk()

v = StringVar()
v.set("lssldfjs")
def show():
    tp = Toplevel()
    tp.title("this is Toplevel")
    tp.geometry("230x100")
    Label(tp,text="sdfasdf",textvariable = v).pack()

Button(root,text = "click",command = show).pack()

mainloop()
