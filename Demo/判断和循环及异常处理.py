fridge={"banala":"B","ptato":"P","orage":"O"};  #只能通过键找到键值
print("输入查询食品名称");
name=input();
"""for key in fridge.keys():#循环键，得到相应键值
     if name==key:
        print("%s食品描述为 %s" % (key,fridge[key]));
        break;
     #elif(fridge.get(name)==None):#字典中无输入字符串，即值为None时，输出无此食品
else:#循环字典使用for——in--else方法，else后的语句为循环完成后所执行
    print("无此食品");
for food in ("a","b","c"):
    if food=="c":
        print("yes");
        break;
else:
    print("no")"""
fridge_list=list(fridge.keys());i=0;#fridge_list.__len__();
while fridge_list:#循环整个列表
    if fridge_list[i]==name:
        print("已找到商品%s" % (fridge_list[i]));
        break;
        fridge_list.pop(i);#弹出第i个元素，列表-1，括号内为则弹出最后一个元素
    else:
        print("无此商品")

