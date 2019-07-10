from tkinter import *

root  = Tk()
enter = Entry(root)
ls = Listbox(root,selectmode = "extended")

v = StringVar()
#l = StringVar()
enter["textvariable"] = v
enter.pack()

def show():
    val = ls.get(ls.curselection())  #返回列表框选定的值
    v.set(val)  #设置在entry显示的值

t = ["chen","li","shen","liu","tang"]
   
for i in t:
    ls.insert(END,i)
ls.pack()


Button(root,text="dddd",command = show).pack()
print(ls.curselection())

mainloop()
