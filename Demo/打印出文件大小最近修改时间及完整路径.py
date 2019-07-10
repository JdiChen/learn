import os
import time
"""def print_path(path):
    for name in os.listdir(path):
        fp = os.path.join(path, name)  #递归得到文件所在目录的完整路径
        if os.path.isfile(fp):
            file_size=os.path.getsize(fp)
            file_time=os.path.getctime(fp)
            print("%s：\n大小为 %dKB\n文件最后修改时间为：%s\n\n" % (os.path.split(fp)[1],file_size,time.ctime(file_time)))
        if os.path.isdir(fp):
            print_path(fp)
print_path(r"D:\ADB\platform-tools")"""
""""
1.打列目录名称
2.打印目录下文件名称
3.按字母顺序排列输出
4.搜索文件是否存在"""
def print_dir(path):
    is_file=[];is_dir=[]
    for file in os.listdir(path):
        full_path =os.path.join(path,file)
        if os.path.isfile(full_path):  #是文件就给a
            is_file.append(full_path)
        elif os.path.isdir(full_path): #是目录就给b
            is_dir.append(full_path)
        else:
            continue
    return (sorted(is_dir),sorted(is_file))
while True:
    path = input("请输入要查询的目录名：")
    if os.path.exists(path):
        a,b=print_dir(path)
        print("%s 下有目录:%s\n文件：%s" % (path,a,b))
        break
    else:
        print("路径不存在，请重新输入：")