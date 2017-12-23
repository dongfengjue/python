#coding=utf-8
import MySQLdb

conn= MySQLdb.connect(
        host='192.168.204.26',
        port = 3306,
        user='root',
        passwd='root',
        db ='c2btest',
        )

cur = conn.cursor()

#创建数据表
#cur.execute("create table student(id int ,name varchar(20),class varchar(30),age varchar(10))")

#插入一条数据
#cur.execute("insert into student values('2','Tom','3 year 2 class','9')")

# pip install mysqlclient
#修改查询条件的数据
#cur.execute("update student set class='3 year 1 class' where name = 'Tom'")

#删除查询条件的数据
#cur.execute("delete from student where age='9'")
cur.execute("select * from orders");
res = cur.fetchall()

results = []

for rec in res:
  results.append(rec[2])

print(results);

# 写入文件
filename = __file__+"\\..\\temp\\sss.txt"
with open(filename, 'w') as f:
  for result in results:
    f.write(str(result) + '\n')


cur.close()
conn.commit()
conn.close()
