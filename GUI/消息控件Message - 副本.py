from tkinter import *
import tkinter.messagebox as msb
root = Tk()
root.geometry("400x300")
v = StringVar()

def show(i):
    if i == "info":
        msb.showinfo(title = "消息",
                    message="123")
    elif i == "warning":
        msb.showwrning()
                    

for i in ["info","warning","error","question",
            "proceed","yes_no","yes_no_cancel","try_again"]:
    bt = Button(root,text = i,
                command = lambda x = i:show(i))
    bt.pack()





mainloop()
