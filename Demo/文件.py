import os
import shutil

def new_verion(path,version):  #返回当前版本文件名
    if version == 0:
        return path
    else:
        return path + "." + str(version) #版本转换为字符串

def up_data(path,version=0):   #更新版本文件
    old_path = new_verion(path,version)
    if not os.path.exists(old_path):
        raise IOError("%s doesn't exitst" % path)
    new_path = new_verion(path,version+1)
    if os.path.exists(new_path):
        up_data(path,version+1)
    shutil.move(old_path,new_path)
"""f=open("E:\\mod\\test.txt","r")
a=f.readlines()
print(a.__len__())
i=1
for line in a:
    print("第%d行为：%s 共%d字" % (i,a[i-1],a[i-1].__len__()))
    i+=1
print(os.path.join("E","mod","test.txt"))
print(os.path.split("E:\\mod\\test.txt"))
f.close()"""

"""def f(path):  #分解文件路径
    a,b=os.path.split(path)
    if b =="":
        return (a, )
    else:
        return f(a)+(b,)
print(f(r"F:\测试工具\LCT_SmartPhone_WriteSNCheck_V5.6.3\DLL\android"))"""

def fileDemo1():
    ds = {}
    with open(os.path.join('e:','IML','test.txt'),'r') as file:
        while file!=None:
            s = file.readline()
            print(s.split('='))
            key,val = s.split('=')
            ds[key] = val
    print(ds)
if __name__ == "__main__":
    fileDemo1()


