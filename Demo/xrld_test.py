import xlrd
import os
f = xlrd.open_workbook(r'E:\IML\longData.xlsx')
t = f.sheet_by_index(0)
col = []

for x in range(1,t.nrows):
    #列表形式显示整个工作表内容
    val = t.row_values(x,0,t.ncols)
    print(val)
    col.append(val)
print(col)