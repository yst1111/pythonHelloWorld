# -*-coding:utf-8-*-
import pymysql
#创建对象
db = pymysql.connect(host='192.168.41.188',user='root',password='root',database='test411',port=3306)
cursor = db.cursor()
# sql语句执性，单行插入
# info_list = ['1','980101','asa','dad']
sql = 'select * from student'
#列表传参
cursor.execute(sql)
re = cursor.fetchall()
for row in re: #遍历
    id = row[0]
    name = row[1]
    print(id+","+name)
db.commit()
# 关闭
cursor.close()
db.close()
