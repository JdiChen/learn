from tkinter import *
root = Tk()

ca = Canvas(root,
       bg = "white",
       width = 300,
       height = 400)
ca.pack()
def pt(event):
    x1,y1 = (event.x-1),(event.y-1)
    x2,y2 = (event.x+1),(event.y+1)
    ca.create_oval(x1,y1,x2,y2,fill = "red")

ca.bind("<B1-Motion>",pt)

Button(root,text = "清除",command = lambda x = ALL:ca.delete(x)).pack()

mainloop()
