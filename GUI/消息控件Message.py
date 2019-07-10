from tkinter import *
root = Tk()
root.geometry("400x300")
v = StringVar()


t = Entry(root)
t.pack()
v.set(t.get())
Message(root,bg = "white",textvariable = v).pack(fill = X)





mainloop()
