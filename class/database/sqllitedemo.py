import sqlite3


db = sqlite3.connect("data.db")

# db.execute("create table emp(id int primary key,name varchar(20),email varchar(50))")

# db.execute("insert into emp values(1,'TISHA','TISHA@gmail.com')")
# db.execute("insert into emp values(2,'TISHA','TISHA@gmail.com')")
# db.execute("INSERT INTO emp VALUES (4, 'RANI', 'RANI@gmail.com')")


# db.execute("update emp set email='TISHA@gmail.com' where id = 1")

db.execute("delete from emp where id=3")

db.commit()
data = db.execute("select * from emp").fetchall()
for dt in data:
    print(dt)