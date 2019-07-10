import sqlite3
#连接数据库
conn = sqlite3.connect(r"E:\IML\SQL\test.db")
curs = conn.cursor()




#建表
sql = """create table if not exists
            stu(id int premary key auto_increment,
            name varchar(20) not null,
            sex varchar(10) not null,
            age int not null,
            phone varchar(20) not null,
            profession varchar(20) not null)"""
curs.execute(sql)
    #查询表print(*curs.execute("select * from sqlite_master"))


#插入数据
def insert_data(id,name,sex,age,phone,profession):
    #sql插入语句，？通配execute内参数
    sql = "insert into stu(id,name,sex,age,phone,profession)\
                        values(?,?,?,?,?,?)"
    try:
        curs.execute(sql,(id,name,sex,age,phone,profession))
        conn.commit()
        print("成功插入学生信息")
    except sqlite3.IntegrityError:
        print("id不能重复，请重新输入")
    except:
        conn.rollback()
        print("事务提交失败")

#更新数据
def update_data(name,val,stuid):
    try:
        if name == "name":
            sql = "update stu set name = ? where id = ?"
        elif name == "sex":
            sql = "updata stu set sex = ? where id = ?"
        elif name == "age":
            int(val)
            sql = "updata stu set age = ? where id = ?"
        elif name == "phone":
            sql = "updata stu set phone = ? where id = ?"
        elif name == "profession":
            sql = "updata stu set profession = ? where id = ?"
        curs.execute(sql,(val,stuid))    
        conn.commit()
        print("更新成功")
    except:
        conn.rollback()
        print("更新失败")

#查找数据    
def select_data(id):
    sql = "select * from stu where id=?"
    re = curs.execute(sql,(id,))
    if len(re.fetchall())!=0:#判断是否有此学号
        for i in curs.execute(sql,(id,)).fetchall():#curs对象查询后只能调用一次，需要重新查询一次才能输出
            show_id = i[0]
            show_name = i[1]
            show_sex = i[2]
            show_age = i[3]
            show_phone = i[4]
            show_profession = i[5]
            print("学号：%d\n姓名：%s\n性别：%s\n年龄：%d\n电话：%s\n专业：%s\n"
                  %(i[0],i[1],i[2],i[3],i[4],i[5]))
    else:
        print("查无此人")
            
   
#删除数据
def del_data(id):    
    sql = "delete from stu where id = ?"
    try:
        curs.execute(sql,(id,))
        conn.commit()
        print("删除成功")
    except:
        conn.rollback()
        print("删除失败")

        
#屏幕显示
def show():
    print("1.插入数据")
    print("2.更新数据")
    print("3.删除数据")
    print("4.查询数据")
    print("5.显示所有学生信息")
    print("6.退出")

#显示学生信息
def show_all_stu():
    curs.execute("select * from stu")
    for i in curs.fetchall():
        show_id = i[0]
        show_name = i[1]
        show_sex = i[2]
        show_age = i[3]
        show_phone = i[4]
        show_profession = i[5]
        print("学号：%d\n姓名：%s\n性别：%s\n年龄：%d\n电话：%s\n专业：%s\n"
              %(i[0],i[1],i[2],i[3],i[4],i[5]))

        
if __name__=="__main__":
    print("请选择数据库操作选项：")
    while True:
        show()
        m = int(input())
        if m == 1:
            print("请在下方输入学生信息")
            id = int(input("学号："))
            name = input("姓名：")
            sex = input("性别：")
            age  = int(input("年龄："))
            phone = input("电话：")
            profession = input("专业：")
            insert_data(id,name,sex,age,phone,profession)
        elif m == 2:            
            update_data(input("输入需要更新的项："),input("输入更新后的值："),input("输入需要更新的学号："))
        elif m == 3:
            del_data(int(input("输入删除id：")))
        elif m == 4:
            select_data(int(input("输入查询id：")))
        elif m == 5:
            show_all_stu()
        elif m == 6:
            break
        print("操作完成，请继续选择：")
    print("谢谢使用")

curs.close()
conn.close()
