import sqlite3
db=sqlite3.connect('emp.db')
cursor=db.cursor()

cursor.execute("select * from employee")

row=cursor.fetchall()
for i in row:
    print(i)
    row=cursor.fetchall()
cursor.close()
db.close()
