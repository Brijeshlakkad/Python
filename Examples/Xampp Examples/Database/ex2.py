#!C:\Users\RAJ\AppData\Local\Programs\Python\Python36\python
import pymysql
db=pymysql.connect("localhost",'root','','brij')
cursor=db.cursor();
sql="select * from users where Name='Brijesh'"
try:
cursor.execute(sql)
data=cursor.fetchall()
if cursor.rowcount==1:
	for row in data:
		id=row[0]
		print("ID : ",id)