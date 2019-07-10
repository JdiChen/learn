from tkinter import *
def set_screen_senter():
    #设置窗口屏幕居中显示
    sw = root.winfo_screenwidth()
    sh = root.winfo_screenheight()
    cw =400
    ch = 300
    x = (sw-cw)/2
    y = (sh-ch)/2-50
    root.geometry("%dx%d+%d+%d" % (cw,ch,x,y))
root = Tk()
root.title("显示")
set_screen_senter()



lsb = Listbox(root)
ent = Entry(root)
for i in range(100):
    lsb.insert(END,i)
lsb.insert(0,"12345fkadflasd;fasd;fkhkahdflkahweufhakljsdghlkajsdhfasdfasdfka")    
scb = Scrollbar(root)
scb2 = Scrollbar(root,
                 orient = "horizontal",#水平显示滚动条
                 command = lsb.xview)#连接至Label
scb3 = Scrollbar(root,
                 orient = "horizontal",#水平显示滚动条
                 command = lsb.xview)#连接至Label
lsb["yscrollcommand"] = scb.set
lsb["xscrollcommand"] = scb2.set#连接至滚动条
ent["xscrollcommand"] = scb3.set
scb3["command"]  =ent.xview
scb["command"] = lsb.yview  


scb.pack(side = RIGHT,fill = Y)
lsb.pack(fill = BOTH)
ent.pack(fill = BOTH)
scb2.pack(side = BOTTOM,fill = X)
scb3.pack(side = BOTTOM,fill = X)
mainloop()

