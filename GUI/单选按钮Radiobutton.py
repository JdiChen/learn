from tkinter import *
def set_screen_senter():
    #设置窗口屏幕居中显示
    sw = root.winfo_screenwidth()
    sh = root.winfo_screenheight()
    cw = 400
    ch = 300
    x = (sw-cw)/2
    y = (sh-ch)/2-50
    root.geometry("%dx%d+%d+%d" % (cw,ch,x,y))



root = Tk()
root.title("显示")
set_screen_senter()    
def show_fruit():
    #显示选中
    for i in range(4):
        if f_val.get() == (i+1):
            win = Tk()
            Label(win,text  = "你喜欢的水果是："+fruit[i][0]).pack()
            Button(win,text = "确定",command = win.destroy).pack()
            
def show_sports():
    #显示选中
    for i in range(4):
        if s_val.get() == (i+1):
            win = Tk()
            Label(win,text  = "你喜欢的运动是："+sports[i][0]).pack()
            Button(win,text = "确定",command = win.destroy).pack()
            
Label(root,text="你喜欢的水果").pack()
fruit = [("苹果",1),("橘子",2),("香蕉",3),("桃子",4)]
sports = [("跑步",1),("篮球",2),("足球",3),("慢跑",4)]
#设置单选默认值，0为不选
f_val = IntVar()
f_val.set(0)
s_val = IntVar()
s_val.set(0)

#创建按钮
for i,j in fruit:
    ckb = Radiobutton(root,
                      text = i,
                      value = j,#单选按钮的后台值
                      variable = f_val,#将值变传给变量
                      command = show_fruit)
    ckb.pack()

Label(root,text="你喜欢的运动").pack()

for i,j in sports:
    rdb = Radiobutton(root,
                      text = i,
                      value = j,
                      variable = s_val,
                      indicatoron = 0,
                      command = show_sports)
    rdb.pack()






mainloop()

