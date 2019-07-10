import xlsxwriter
wk = xlsxwriter.Workbook("writer_test.xlsx")
st = ["sfd","adfa","asdfadf","ccccccff"]
dd = {"qqq":"est","wwww":"gghj","jjj":"hvnv"}
t = wk.add_worksheet("写入测试")
t.write(0,4,"python")
t.write(0,1,"qer")
t.write(5,5,"opeo")
t.insert_image(10,10,r"E:\图片\123.jpg")
t.write_row(1,1,dd.keys())
t.write_row(2,1,dd.values())
wk.close()
