from tkinter import *

root = Tk()

def show(text):
    return text

v = IntVar()
Scale(root,label = "thiw",from_=10,to_=100,
      #resolution = 10,
      orient = "horizontal",#设置水平方向，默认垂直
      variable = v,
      command = show,
      #digits = 9,#设置整个显示位数
      tickinterval = 5,
      length = 500).pack()
Label(root,textvariable = show(v)).pack()

mainloop()
