import sqlite3
db=sqlite3.connect('company.db')
cursor=db.cursor()
table=[dno INTEGER primary key,dname TEXT]
cursor.execute("create table if not exists dept{}".format(table))
cursor.execute("create table emp(eno integer primary key,ename text,basic float,hra float,da float,pf float,d_no integer),FOREIGN KEY (d_no) references dept(dno)")
cursor.execute("insert into dept values(1,'IT')")
cursor.execute("insert into dept values(2,'comps')")
cursor.execute("insert into dept values(3,'mech')")
cursor.execute("insert into dept values(4,'extc')")
cursor.execute("insert into emp values(1,'prit',1000,20,30,40,1)")
cursor.execute("insert into emp values(2,'neha',2000,20,30,40,4)")
cursor.execute("insert into emp values(3,'parth',700,20,30,40,3)")

db.commit()


