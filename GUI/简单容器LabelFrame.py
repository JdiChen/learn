from tkinter import *
root = Tk()
lf1 = LabelFrame(root,
                 width = "300",
                 height = "100",
                 text = "1").grid(row = 0,column = 0)
lf2 = LabelFrame(root,
                 width = "300",
                 height = "100",
                 text = "2").grid(row = 1,column = 0)
lf3 = LabelFrame(root,
                 width = "100",
                 height = "200",
                 text = "3").grid(row = 0,column = 1,rowspan = 2)
en = Entry(lf1)
en.grid(row = 1,column = 0)

mainloop()
