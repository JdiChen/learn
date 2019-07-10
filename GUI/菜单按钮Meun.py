from tkinter import *

root = Tk()




main_menu = Menu(root)

file_menu = Menu(main_menu,tearoff = 0)

edit_menu = Menu(main_menu,tearoff = 0)

run_menu = Menu(main_menu,tearoff = 0)

op_menu = Menu(main_menu,tearoff = 0)

def show():
   
    for o in [undo.get(),
              redo.get(),
              copy.get(),
              pause.get(),
              select_all.get(),
              cut.get()]:
        if o==0:
            print(o)
        else:
            print(o)
    print("显示完成\n\n")
def show_run():
    print(run_val.get())
undo = StringVar()
redo = StringVar()
copy = StringVar()
cut = StringVar()
pause = StringVar()
select_all = StringVar()

def nothing():
    win = Toplevel(root)
    Button(win,text="do nothion").pack()

run_val = StringVar()
run_val.set("run")
for i in ["new file","open file","save","save as","exit"]:
    #子菜单显示
    file_menu.add_command(label=i)
    
    #添加checkbutton菜单
for k,v in  {"undo":undo,
             "redo":redo,
             "copy":copy,
             "cut":cut,
             "pause":pause,
             "select all":select_all}.items():
    if k=="copy":
        edit_menu.add_separator()#添加分隔符
    edit_menu.add_checkbutton(label = k,variable = v,command = show,onvalue = k)

    
    #添加radiobutton菜单
for r in [("run"),"run for cmd","run for win"]:
    run_menu.add_radiobutton(label = r,variable = run_val,command =show_run)

    

for o in ["help","关于","nothing"]:
    op_menu.add_command(label=o,command = nothing)

    
#将子菜单添加至主菜单上
main_menu.add_cascade(label="File",menu = file_menu,)
main_menu.add_cascade(label="Edit",menu = edit_menu,)
main_menu.add_cascade(label="Run",menu = run_menu,)
main_menu.add_cascade(label="Option",menu = op_menu,)

root["menu"] =main_menu

mainloop()
