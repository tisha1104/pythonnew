#========================================>Lab-1<==================================================
#========================================> Printing on Screen <===================================

# Q-1. Write a Python program to print a formatted string using print() and f-string. 

Name="Tisha"
age=20

print(f"My Name is {Name} and i am {age} year old")


# ------------------------------------------------->Practical Examples:<-------------------------------

# Q-1. Write a Python program to print “Hello, World!” on the screen.

print("Hello World!")



#========================================>Lab-2<==================================================
#========================================>Reading Data from Keyboard<=============================

#Q-1. Write a Python program to read a name and age from the user and print a formatted output. 

Name=input("Enter Your Name:- ")
age=int(input("Enter Your Age:- "))

print(f"Hello, {Name}! you are {age} Year Old")



# ------------------------------------------------->Practical Examples:<-------------------------------

# Q-2. Write a Python program to read a string, an integer, and a float from the keyboard and display them.

Name=input("Enter Youre Name:- ")
Age=int(input("Enter Youre Age:- "))
Height=float(input("Enter Youre Height:- "))
print(f"Hello,{Name}! You Are {Age} Year Old and Your Height is {Height}")



#========================================>Lab-3<==================================================
#========================================>Opening and Closing Files<==============================

# Q-1. Write a Python program to open a file in write mode, write some text, and then close it.

f=open("test.txt",'w')
f.write("Hello World!")
f.close 


# ------------------------------------------------->Practical Examples:<-------------------------------

# Q-3. Write a Python program to create a file and write a string into it.

f=open("My_program",'w')
f.write("Hello Python! \nHello C++! \nHello C! ")
f.close



#========================================>Lab-4<==================================================
#========================================> Reading and Writing Files <==============================

# Q-1. Write a Python program to read the contents of a file and print them on the console. 

f=open("My_program",'r')
data=f.read()
print(data)


# Q-2. Write a Python program to write multiple strings into a file. 

with open("test.txt",'w')as f:
    f.write("""Hello World!
Hello Python
Hello Java
Hello C++
            """)
    

# ------------------------------------------------->Practical Examples:<-------------------------------

#Q-4. Write a Python program to create a file and print the string into the file.  

with open("Demo.txt",'w')as f:
    f.write(" Hello World!, My Name Is Tisha")


#Q-5. Write a Python program to read a file and print the data on the console. 

with open("Demo.txt",'r') as R:
    data=R.read()
    print(data)


# Q-6. Write a Python program to check the current position of the file cursor using tell().

with open("Demo.txt",'r') as R:
    data=R.read()
    print(R.tell())


#========================================>Lab-5<=====================================================
#========================================>Exception Handling<========================================

#Q-1. Write a Python program to handle exceptions in a simple calculator (division by zero, invalid input).

def Calculator():
    try:
        Number1= float(input("Enter The Number1: "))
        Number2= float(input("Enter The Number2: "))
        option=input("Choose Right Option: ")

        if option=='+':
            result=Number1+Number2
        elif option=='-':
            result=Number1-Number2
        elif option=='*':
            result=Number1*Number2
        elif option=='/':
            result=Number1/Number2
        else:
            raise ValueError("Invalid Option:")
        print("Result: ",result)

    except ZeroDivisionError:
        print("Error: Division by Zero is not allowed.")
    except ValueError:
        print("Error: Please enter valid numbers.")
    finally:
        print("Calculation attempt completed")

Calculator()


#Q-2. Write a Python program to demonstrate handling multiple exceptions. 

def multiple_exception():
    try:
        number =[1,2,3]
        num=int(input("Enter index: "))
        result=number[num]/(int(input("Enter a divisor:")))
        print("Result: ",result)
    except IndexError:
        print("Error: Index Out Of range.")
    except ZeroDivisionError:
        print("Error: Division by Zero is not allowed")
    except ValueError:
        print("Error: Please enter Valid integers")
    finally:
        print("Operation Completed.")

multiple_exception()


# ------------------------------------------------->Practical Examples:<-------------------------------

#Q-7. Write a Python program to handle exceptions in a calculator.

def Calculator():
    try:
        Number1= float(input("Enter The Number1: "))
        Number2= float(input("Enter The Number2: "))
        option=input("Choose Right Option: ")

        if option=='+':
            result=Number1+Number2
        elif option=='-':
            result=Number1-Number2
        elif option=='*':
            result=Number1*Number2
        elif option=='/':
            result=Number1/Number2
        else:
            raise ValueError("Invalid Option:")
        print("Result: ",result)

    except ZeroDivisionError:
        print("Error: Division by Zero is not allowed.")
    except ValueError:
        print("Error: Please enter valid numbers.")
    finally:
        print("Calculation attempt completed")

Calculator()


#Q-8. Write a Python program to handle multiple exceptions (e.g., file not found, division by zero). 

try:
    with open("Demo.txt",'r')as R:
        data=R.read()
        print(data)

    a=input("Enter the value of a: ")
    b=input("Enter the value of b: ")
    result=a/b
    print("Result: ",result)
except FileNotFoundError:
    print("Error: The file was not found.")
except ZeroDivisionError:
    print("Error: Division by Zero is not allowed.")
except ValueError:
    print("Error: Please enter valid numbers.")
except Exception as e:
    print("Unexcepted error:",e)
finally:
    print("Your Program excuted Suceesfully:")


# Q-9. Write a Python program to handle file exceptions and use the finally block for closing the file.

f=""
try:
    f=open("test.txt","r")
    data=f.read()
    print(data)
except Exception as a:
    print(a)
finally:
    if(f is not None):
        f.close()


#Q-10. Write a Python program to print custom exceptions. 

print("program Start...")
try:
    num=int(input("Enter The Positive Number: "))
    if num<0:
        raise Exception("custom Exception: Negative number are not allowed!")
    else:
        print("You Enter Valid Number: ",num)
except Exception as e:
    print(e)
finally:
    print("Program Ended...")


#========================================>Lab-6<=======================================================
#========================================>Exception Handling<==========================================

# Q-1. Write a Python program to create a class and access its properties using an object.

class Student:

    id=11
    Name="Tisha"
    email="Tisha@gmail.com"
    Phone=8866068695

    def display(self):
        print("id=",self.id)
        print("Name=",self.Name)
        print("email=",self.email)
        print("Phone=",self.Phone)

Recoerd=Student()
Recoerd.display()

print("*********************************************")

Recoerd1=Student()
Recoerd1.id=12
Recoerd1.Name="Rani"
Recoerd1.email="Rani@gmail.com"
Recoerd1.Phone=8569632785
Recoerd1.display()


# ------------------------------------------------->Practical Examples:<-------------------------------

# Q-11. Write a Python program to create a class and access the properties of the class using an object.

class Pen:
    id=101
    color="Black"
    company="S.S"

    def display(self):
        print("id=",self.id)
        print("color=",self.color)
        print("company=",self.company)

P=Pen()
P.display()

print("**************************************")
P1=Pen()
P1.id=102
P1.color="Blue"
P1.company="Cello"
P1.display()


# Q-12.  Write a Python program to demonstrate the use of local and global variables in a class.

company="Tech_Word"               #global varibale

class Employee:
    
    def __init__(self,name,slary):
        self.name=name
        self.slary=slary

    def Show_Details(self):
        bonus=2500                    #local varibale
        print("Company Name=",company)
        print("Employee Name=",self.name)
        print("Slary=",self.slary)
        print("Bonus=",bonus)
      

E=Employee("Tisha",25000)
E.Show_Details()

E1=Employee("Rani",22000)
E1.Show_Details()


#========================================>Lab-7<=====================================================
#========================================>Inheritance<===============================================

#Q-1.Write Python programs to demonstrate different types of inheritance (single, multiple, multilevel, etc.). 

# ====>Single inheritance :-

class pen:
    price=100
    color="Red"
    company="Cello"

    def display(self):
        print(self.price,self.color,self.company)

class Notebook(pen):
    Pages=100

    def show(self):
        self.price=50
        print(self.price,self.color,self.company,self.Pages)

p=pen()
p.display()
n=Notebook()
n.show()


#====>Hierarchical Inheritance:-

# class Animal ():
#     def details(self):
#         self.Name=input("Enter The Animal Name: ")

# class Eating(Animal):
#     def eat(slef):
#         print(f"{slef.Name} is Eating")

# class slepping(Animal):
#     def sleep(self):
#         print(f"{self.Name} is Sleeping")

# e=Eating()
# e.details()
# e.eat()

# s=slepping()
# s.details()
# s.sleep()


#====>Multilevel inheritance:-

# class Animal:
#     def details(self):
#         self.Name=input("Enter The Animal Name: ")

# class Eating(Animal):
#     def eat(slef):
#         print(f"{slef.Name} is Eating")

# class slepping(Eating):
#     def sleep(self):
#         print(f"{self.Name} is Sleeping")

# a=slepping()
# a.details()
# a.eat()
# a.sleep()


#====>Multiple Inheritance :-

class Animal ():
    def details(self):
        self.Name=input("Enter The Animal Name: ")

class Eating:
    def eat(slef):
        print(f"{slef.Name} is Eating")

class slepping:
    def sleep(self):
        print(f"{self.Name} is Sleeping")

class Animale_Activity(Animal,Eating,slepping):
    pass

A1=Animale_Activity()
A1.details()
A1.eat()
A1.sleep()


# ---------------------------------->Practical Examples:<-------------------------------

# Q-13.Write a Python program to show single inheritance. 

class person:
    def details(self):
        self.name=input("Enter person name: ")

class Infoermation(person):
    def show(self):
        print(f"This Infoermation is about {self.name}")

i=Infoermation()
i.details()
i.show()


# Q-14.Write a Python program to show multilevel inheritance.

class person:
    def details(self):
        self.name=input("Enter person name: ")

class Infoermation(person):
    def show(self):
        print(f"This Infoermation is about {self.name}")

class chek_identiy(Infoermation):
    def chek(self):
        print(f"{self.name} is Student")


c=chek_identiy()
c.details()
c.show()
c.chek()


# Q-15. Write a Python program to show multiple inheritance. 

class person:
    def details(self):
        self.name=input("Enter person name: ")

class Infoermation:
    def show(self):
        print(f"This Infoermation is about {self.name}")

class chek_identiy:
    def chek(self):
        print(f"{self.name} is Student")

class clg(person,Infoermation,chek_identiy):
    def clg_details(self):
        print(f"{self.name} is study in clg")

c1=clg()
c1.details()
c1.show()
c1.chek()
c1.clg_details()


# Q-16. Write a Python program to show hierarchical inheritance.

class person:
    def details(self):
        self.name=input("Enter person name: ")

class Infoermation(person):
    def show(self):
        print(f"This Infoermation is about {self.name}")

class clg(Infoermation):
    def clg_details(self):
        print(f"{self.name} is study in this clg")

i1=Infoermation()
i1.details()
i1.show()

c1=clg()
c1.details()
c1.clg_details()


# Q-17. Write a Python program to show hybrid inheritance.

class Animal:
    def details(self):
        self.Name=input("Enter The Animal Name: ")

class Eating(Animal):
    def eat(slef):
        print(f"{slef.Name} is Eating")

class slepping(Animal):
    def sleep(self):
        print(f"{self.Name} is Sleeping")

class Animale_Activity(Eating,slepping):
    def Activity(self):
        print(f"{self.Name} can eat and sleep both")

a1=Animale_Activity()
a1.details()
a1.eat()
a1.sleep()
a1.Activity()

# Q-18.  Write a Python program to demonstrate the use of super() in inheritance.

class Animal:
    def __init__(self,name):
        self.name=name 
        print("Animal constructor called....")

class Dog(Animal):
    def __init__(self, name,breed):
        super().__init__(name)
        self.breed=breed
        print("Dog constructor called....")

    def show(self):
        print(f"{self.name} is a {self.breed}")

d1= Dog("Lily","Bulldog")
d1.show()


#========================================>Lab-8<===========================================
#===========================> Method Overloading and Overriding<===========================


# Q-1. Write Python programs to demonstrate method overloading and method overriding. 

# ==>Overloading

class Calculator:
    def add(self,a=0,b=0,c=0):
        return a+b+c

calc = Calculator()
print(calc.add(2))       
print(calc.add(2,3))     
print(calc.add(2,3,4))

# ==>Overriding

class Animal:
    def sound(self):
        print("Animal makes different sounds")

class Dog:
    def sound(self):
        print("Dog barks")

a= Animal()
d= Dog()

a.sound()
d.sound()


# ---------------------------------->Practical Examples:<-------------------------------

# Q-19.  Write a Python program to show method overloading. 

class AreaCalculator:
    def area(self,a=0,b=0):
        if a!=0 and b!=0:
            print("Area of Rectangle: ",a*b)
        elif a!=0:
            print("Area of Square: ",a*a)
        else:
            print("No value given")

a11=AreaCalculator()
a11.area(11)
a11.area(5,10)
a11.area()


# Q-20. Write a Python program to show method overriding.

class Vehicle:
    def show(self):
        print("this is a vehicle") 

class car(Vehicle):
    def show(self):
        print("this is a car")

v1= Vehicle()
v2=car()

v1.show()
v2.show()