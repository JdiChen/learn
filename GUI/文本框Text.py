from tkinter import *
root = Tk()

t = Text(root)
s = Scrollbar(root)
s["command"] = t.yview
t["yscrollcommand"] = s.set

for i in range(10):
    t.insert(END,"%d****\n" % (i+1))

def inserttext():
    t.insert(INSERT,"####")

def currenttext():
    t.insert(CURRENT,"###4")

def endtext():
    t.insert(END,"1##4")
    
def lasttext():
    t.insert(SEL_LAST,"kldf####sdfa")
    
def firsttext():
    t.insert(SEL_FIRST,"asdf####dfad")

Button(root,
       text = "insert",
       command = inserttext).pack(side = BOTTOM,fill = X)
Button(root,
       text = "current",
       command = currenttext).pack(side = BOTTOM,fill = X)
Button(root,
       text = "end",
       command = endtext).pack(side = BOTTOM,fill = X)
Button(root,
       text = "sel_last",
       command = lasttext).pack(side = BOTTOM,fill = X)
Button(root,
       text = "sel_first",
       command = firsttext).pack(side = BOTTOM,fill = X)


t.pack(side = LEFT,fill = BOTH)
s.pack(side = RIGHT,fill = Y)
root.mainloop()
