import mysql.connector

conn=mysql.connector.connect(
	host="localhost",
	username="root",
	password="Mysql@123")

cursor=conn.cursor()

query="""CREATE database if not exists books_library_db"""

cursor.execute(query)

query="""SHOW databases"""

cursor.execute(query)

result=cursor.fetchall()

for r in result:

	print(r[0])

conn.commit()

cursor.close()

conn.close()