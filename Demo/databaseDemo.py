import pymysql


conn = pymysql.connect('127.0.0.1','root','root','mysql',charset='utf8')
sql = 'select * from event'
#sql = 'show create database test'

cor = conn.cursor();
#cor.query('set names utf8')
cor.execute(sql)
#这里读出来就是乱码 fetcahll是返回sql查询的所有数据，以列表方式返回
for i in cor.fetchall():
    print(i[0],i[1]);
conn.close();
