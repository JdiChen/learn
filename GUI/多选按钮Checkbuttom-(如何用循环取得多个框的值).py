from tkinter import *
def set_screen_senter():
    #设置窗口屏幕居中显示
    sw = root.winfo_screenwidth()
    sh = root.winfo_screenheight()
    cw = 400
    ch = 400
    x = (sw-cw)/2
    y = (sh-ch)/2-50
    root.geometry("%dx%d+%d+%d" % (cw,ch,x,y))
    



def ifall():#全选操作
    if al.get() == 1:
        for i in list_ckb:
            i.select()
    if al.get() == 0:
        for i in list_ckb:
            i.deselect()
            
def show(n):#显示勾选的哪些项
    q = IntVar()
    q = []    
    root2 = Tk()
    root2.title("已选中选项")
    root2.geometry("200x80")    
    for i in n:
        z = i.get()
        if z != 0:
            q.append(z)
    
    Label(root2,text = str(*q),bg = "white").pack()
    
   
    
root = Tk()
root.title("显示")
set_screen_senter()    

list_num = [1,2,3,4,5,6,7,8,9]  #checkbutton显示列表
list_ckb = []   #checkbutton存储列表
al = IntVar()  #全选框接收值
n = []
for i in ['a','b','c','d','e','f','g','j','k']:
    i = StringVar()
    n.append(i)

p = IntVar()

#创建复选框
for i in list_num:
    j = 0
    #建立复选框，并把勾选的值设置为显示值
    ckb = Checkbutton(root,
                      text = i,
                      onvalue = i,
                      variable = n[j],
                      )
    #将新建的checkbutton插入至列表
    j+=1
    list_ckb.append(ckb)                  

    ckb.pack(anchor=W)
     
print(*n)
#建立全选按钮
se_all = Checkbutton(root,text="全选",variable = al,command = ifall)
se_all.pack(anchor=E)



lb = Label(root,textvariable = p)
lb.pack()

bt = Button(root,text="确定",command=lambda x=n:show(x)).pack()
mainloop()

