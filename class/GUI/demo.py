from tkinter import *

root = Tk()
root.geometry("700x500")


l1 = Label(root,text="name").place(x=200,y=100)
l2 = Label(root,text="email").place(x=200,y=150)
l3 = Label(root,text="phone").place(x=200,y=200)

e1 = Entry(root).place(x=300,y=100)
e2 = Entry(root).place(x=300,y=150)
e3 = Entry(root).place(x=300,y=200)
e1 = Entry(root)
e1.place(x=300,y=100)
e2 = Entry(root)
e2.place(x=300,y=150)
e3 = Entry(root)
e3.place(x=300,y=200)

b1  =Button(root,text="submit",width=15).place(x=300,y=230)
b1  =Button(root,text="submit",width=15).place(x=300,y=230)

root.mainloop()