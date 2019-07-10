from tkinter import *
root = Tk()
root.title("登录界面")
def set_screen_center():
    sw = root.winfo_screenwidth()
    sh = root.winfo_screenheight()
    cw = 400
    ch = 300
    x = (sw-cw)/2
    y = (sh-ch)/2-50
    root.geometry("%dx%d+%d+%d" % (cw,ch,x,y))
set_screen_center()
    

def show_msg():
    print("用户名：%s\n密码：%s" % (us_enter.get(),ps_enter.get()))

#user_val = StringVar()
#ps_val = StringVar()

user = Label(root,text = "用户名").grid(row = 0,column = 0)
password = Label(root,text = "密 码").grid(row = 1,column = 0)

us_enter = Entry(root)
us_enter.grid(row = 0,column = 1)          
ps_enter = Entry(root,show="#")
ps_enter.grid(row = 1,column = 1)

login = Button(root,text = "登录",command = show_msg).grid(row = 2,column = 0)
login2 = Button(root,text = "退出",command = root.destroy).grid(row = 2,column = 1)


mainloop()
