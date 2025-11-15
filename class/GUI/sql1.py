from tkinter import *
from tkinter import ttk,messagebox
import mysql.connector as sql

root= Tk()

root.geometry("700x600")


def insert():
    name= e1.get()
    email=e2.get()
    phone=e3.get()

    con=sql.connect(
    host="localhost",
    user="root",
    password= "tisha",
    port="3306",
    database="Schhol"
)

    cursor =con.cursor()
    # cursor.execute("create database Schhol")
    # cursor.execute("create table studet(id int primary key auto_increment,name varchar(50),email varchar(50),phone varchar(50))")

    qry="insert into studet (name ,email,phone) values (%s,%s,%s)"
    values=(name,email,phone)
    cursor.execute(qry,values)
    con.commit()
    print("data inserted")
l1=Label(root,text="Name").place(x=300,y=200)
l2=Label(root,text="email").place(x=300,y=250)
l3=Label(root,text="phone").place(x=300,y=300)



e1= Entry(root)
e1.place(x=350,y=200)
e2= Entry(root)
e2.place(x=350,y=250)
e3= Entry(root)
e3.place(x=350,y=300)

b1=Button(root,text="submit",command=insert).place(x=350,y=350)

cols=("id","name","email","phone")
table=ttk.Treeview(root,columns=cols,show="headings")
for col in cols:
    table.heading(col,text=col)
    table.place(x=10,y=400)
root.mainloop()