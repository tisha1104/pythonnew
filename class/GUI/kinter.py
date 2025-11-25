from tkinter import *
import mysql.connector as sql
root = Tk()
root.geometry("700x500")

# b1 = Button(root,text="LEFT").pack(side=LEFT)
# b2 = Button(root,text="right").pack(side=RIGHT)
# b3 = Button(root,text="TOP").pack(side=TOP)
# b4 = Button(root,text="BOTTOM").pack(side=BOTTOM)


# l1 = Label(root,text="name").grid(row=1,column=1)
# l2 = Label(root,text="email").grid(row=2,column=1)
# l3 = Label(root,text="phone").grid(row=3,column=1)

# e1 = Entry(root).grid(row=1,column=2)
# e2 = Entry(root).grid(row=2,column=2)
# e3 = Entry(root).grid(row=3,column=2)

# b1  =Button(root,text="submit").grid(row=4,column=2)

def insert():
    name =  e1.get()
    email = e2.get()
    phone = e3.get()

    con =sql.connect(
        host="localhost",
        user = "root",
        password = "tisha",
        port =3306,
        database="Python"
    )
    cursor = con.cursor()
    cursor.execute(
    "INSERT INTO student (name, email, phone) VALUES (%s, %s, %s)",
    ("John", "john@example.com", "1234567890")
)
    con.commit()
    print("data inserted")
  

l1 = Label(root,text="name").place(x=200,y=100)
l2 = Label(root,text="email").place(x=200,y=150)
l3 = Label(root,text="phone").place(x=200,y=200)

e1 = Entry(root)
e1.place(x=300,y=100)
e2 = Entry(root)
e2.place(x=300,y=150)
e3 = Entry(root)
e3.place(x=300,y=200)

b1  =Button(root,text="submit",command=insert,width=15).place(x=300,y=230)

root.mainloop()