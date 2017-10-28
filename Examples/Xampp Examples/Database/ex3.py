#!C:\Users\RAJ\AppData\Local\Programs\Python\Python36\python
import pymysql
db=pymysql.connect("localhost",'root','','brij')
cursor=db.cursor();
sql="insert into users (Name,Password) values ('raj','123456')"
try:
	cursor.execute(sql)
	db.commit()
except:
	db.rollback()
	
	
db.close()