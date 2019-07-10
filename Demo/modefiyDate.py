import re
import os
import random
#创建文件
def createFile():
    for i in range(1,100):
        DD = random.randint(1,30)
        MM = random.randint(1,12)
        YYYY = random.randint(1000,9999)
        filename =str(DD)+'_'+str(MM)+'_'+str(YYYY)+'.txt'
        path = os.path.join('e:','test',filename)
        f = open(path,'w+')

t = '[\d]{1,2}_[\d]{1,2},[\d]{1,4}'
s = '26_10_8346'
print( re.fullmatch(t,s))

