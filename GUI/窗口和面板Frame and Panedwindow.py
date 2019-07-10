from tkinter import *
root = Tk()
p = PanedWindow(orient = "vertical")
p.pack(fill = BOTH,expand = 1)

for w in [Label,Button,Checkbutton,Radiobutton]:
    p.add(w(p,text = "one",bg = "blue"))
p.add(Entry(p))

mainloop()
