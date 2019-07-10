from tkinter import *
import tkinter.messagebox as msb
root = Tk()
v = StringVar()
v.set("show")
def show(i):
    if i == "info":
        m = msb.showinfo(title = "提示消息",message = "info")
        v.set(str(m)+"-"+str(type(m)))
        
    elif i == "warning":
        m = msb.showwarning(title = "提示消息",message = "warning")
        v.set(str(m)+"-"+str(type(m)))
    elif i == "question":
        m = msb.askquestion(title = "提示消息",message = "askquestion")
        v.set(str(m)+"-"+str(type(m)))
    elif i == "proceed":
        m = msb.askokcancel(title = "提示消息",message = "askokcancle")
        v.set(str(m)+"-"+str(type(m)))
    elif i == "yes_no":
        m = msb.askyesno(title = "提示消息",message = "askyesno")
        v.set(str(m)+"-"+str(type(m)))
    elif i == "yes_no_cancel":
        m = msb.askyesnocancel(title = "提示消息",message = "askyesnocancel")
        v.set(str(m)+"-"+str(type(m)))
    elif i == "try_again":
        m = msb.askretrycancel(title = "提示消息",message = "askretrycancel")
        v.set(str(m)+"-"+str(type(m)))
    elif i == "error":
        m = msb.showerror(message = "showerror")
        v.set(str(m)+"-"+str(type(m)))
               
    
for i in ["info","warning","error","question",
             "proceed","yes_no","yes_no_cancel","try_again"]:
    bt = Button(root, text=i,)
    bt["command"]=lambda x=bt: show(x.cget("text"))
    
    bt.pack(fill = BOTH)

"""b1 = Button(root,text = "info",command = info).pack(fill = BOTH)
b2 = Button(root,text = "warning",command = warning).pack(fill = BOTH)
b3 = Button(root,text = "askquestion",command = question).pack(fill = BOTH)
b4 = Button(root,text = "askokcancle",command = okcancel).pack(fill = BOTH)
b5 = Button(root,text = "askyesno",command = yes_no).pack(fill = BOTH)
b6 = Button(root,text = "askyesnocancel",command = yes_no_cancel).pack(fill = BOTH)
b7 = Button(root,text = "askretrycancel",command = try_cancel).pack(fill = BOTH)
b8 = Button(root,text = "showerror",command = error).pack(fill = BOTH)"""

Label(root,textvariable = v,bg="white").pack(fill = BOTH)




mainloop()
