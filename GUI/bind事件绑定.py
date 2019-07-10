from tkinter import *
root = Tk()
v= StringVar()
v.set("32")
def show(event):
    #print(event.x,event.y)
    v.set(str(event.x)+"x"+str(event.y))

def show2(event):
    #print(event.char)
    v.set(event.char)
    
fm = Frame(root,
       bg = "white",
       width = 200,
       height = 200)
#fm.bind("<Button-1>",show)
fm.bind("<Motion>",show)
fm.bind("<Key>",show2)
fm.focus_set()  
lb  = Label(root,textvariable = v)


fm.pack()
lb.pack()
root.mainloop()
