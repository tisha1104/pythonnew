# ==================================================>Lab-1<==============================================================
# ==================================================>Accessing List<=====================================================

#Q-1.Write a Python program to create a list with elements of multiple data types (integers, strings, floats, etc.).

l=["Tisha","Rani",10,20,30,40,50,10.5,11.11,12.58,"5x","11y"]
# print(l)

# for i in l:
#     print(i)

# for i in range(len(l)):
#     print(l[i])


#Q-2.Write a Python program to access elements at different index positions. 

# print(l[0])
# print(l[2:6])
# print(l[-1])
# print(l[-5])
# print(l[:8])
# print(l[4:])
# print(l[-4:-1])


# ----------------------------------------------------->Practical Examples:<--------------------------------------

#Q-1.Write a Python program to create a list of multiple data type elements.

# l1=["Python","Java","C++","C",10,20,30,410,555,50,60,80,11.11,15.8,1.5,8.9,"5J","10X","16Y","20Z"]
# print(l1)

# for i in l1:
#     print(i)

# for i in range(len(l1)):
#     print(l1[i])


#Q-2.Write a Python program to find the length of a list using the len() function.

# list=["Tisha","Rani","Zeel","Devanshi","Nidhi",105,11,158,280,96,11.5,52.8,"5X","10Y","11Z"]
# print(len(list))


# ==================================================>Lab-2<==============================================================
# ==================================================>List Operations<=====================================================

#Q-1.Write a Python program to add elements to a list using insert() and append(). 

# list1=["Python","java","C"]
# list1.insert(1,"C++")
# print(list1)
# list1.append("SQL")
# print(list1)


#Q-2.Write a Python program to remove elements from a list using pop() and remove(). 

# list2=["Tisha","Rani","Rddhi","Nidhi","Ishika"]
# list2.remove("Rddhi")
# print(list2)
# list2.pop(4)
# print(list2)


# ----------------------------------------------------->Practical Examples:<--------------------------------------

#Q-3.Write a Python program to update a list using insert() and append().

# l=["Mango","Banana","Charry"]
# l.insert(0,"Graphs")
# print(l)
# l.append("Water Malooen")
# print(l)


#Q-4.Write a Python program to remove elements from a list using pop() and remove().

# l1=["Rabiit","Dog","Cat"]
# l1.insert(0,"Mouse")
# print(l1)
# l1.append("Peg")
# print(l1)


# ==================================================>Lab-3<==============================================================
# ==================================================> Working with Lists <=====================================================

#Q-1.Write a Python program to iterate over a list using a for loop. 

# fruit=["Mango","Apple","Banana","Charry","Dragon Fruit","Lichi"]

# for fruit in fruit:
#     print(fruit)


#Q-2.Write a Python program to sort a list using both sort() and sorted(). 

fruit=["Mango","Apple","Banana","Charry","Dragon Fruit","Lichi"]

# fruit.sort()
# fruit.sort(reverse=True)
# sorted(fruit)
# print(fruit)


# ----------------------------------------------------->Practical Examples:<--------------------------------------

#Q-1.Write a Python program to iterate through a list and print each element.

# Birds=["Peacock","Parrot","Owl","Eagle","Pigeon","Sparrow","Duck","Swan"]

# for Birds in Birds:
#     print(Birds)


#Q-2. Write a Python program to insert elements into an empty list using a for loop and append().

# List=[]
# n=int(input("Enter the Number of elements "))

# for i in range(n):
#     elements=input(f"Enter the elements{i+1} ")
#     List.append(elements)
# print(List)


#==================================================>Lab-4<==============================================================
# ==================================================>  Tuple  <========================================================

#Q-1.Write a Python program to create a tuple with multiple data types.

# t=(10,20,30,40,50,50,60,710,"Tisha","Rani",False,True,11.11,10.96,8.1,"5J","10X","11Y")
# print(t)


#Q-2.Write a Python program to concatenate two tuples. 

# t1=(10,20,30,40,50,60,70,100)
# t2=(110,120,230,140,14.52,11.11)

# t3=t1+t2
# print(t3)


# ----------------------------------------------------->Practical Examples:<--------------------------------------

#Q-1.Write a Python program to convert a list into a tuple. 

list=["Python","java","C","C++"]
# print(type(list))
t=(tuple(list))
print(t)
print(type(t))


#Q-2.Write a Python program to create a tuple with multiple data types. 

t=(10,20,30,100,"Tisha","Rani",55.12,11.11,8.00,9.5,"5X","10Y","11Z",True,False,"Red","Black")
print(t)


#Q-3.Write a Python program to concatenate two tuples into one.

a=("Red","Black","Yellow")
b=("Greay","Pink","White")

c=a+b
print(c)


#Q-4.Write a Python program to access the value of the first index in a tuple. 

t1=("Python","Java","C","C++")
print(t1[0])
print(t1[1])


#==================================================>Lab-5<================================================================
# ==================================================>Accessing Tuple<===================================================

#Q-1.Write a Python program to access values between index 1 and 5 in a tuple. 

a=("Computer","Mouse","CPU","Key-Board","Hard-disk","Pen-drive","T.V")
print(a[1:6])


#Q-2.Write a Python program to access alternate values between index 1 and 5 in a tuple.

b=(10,20,30,40,50,60,70,80,90)
print(b[1:6:2])


# ----------------------------------------------------->Practical Examples:<--------------------------------------

#Q-1. Write a Python program to access values between index 1 and 5 in a tuple.

c=(100,200,300,400,500,600,700,800,900,1000)
print(c[1:6])


#Q-2. Write a Python program to access the value from the last index in a tuple. 

A=(10,20,30,40,50,60,70,80,90,100)
print(A[-1])


#==================================================>Lab-6<================================================================
#==================================================>Dictionaries<=========================================================

#Q-1.Write a Python program to create a dictionary with 6 key-value pairs. 

T={"Name":"Tisha",
    "email":"tishapatel@gmail.com",
    "Phone":"8563239710",
    "Age":"20",
    "Subject":"Python",
    "Duration":"1 Year"
    }
print(T)


#Q-2.Write a Python program to access values using dictionary keys. 

T2={"Name":"Rani",
    "email":"Ranipatel@gmail.com",
    "Phone":"8113239710",
    "Age":"20",
    "Subject":"C,C++",
    "Duration":"3 Month"
    }
print(T2["Name"])
print(T2["email"])
print(T2["Phone"])
print(T2["Age"])
print(T2["Subject"])
print(T2["Duration"])


# ----------------------------------------------------->Practical Examples:<--------------------------------------

#Q-1.Write a Python program to create a dictionary of 6 key-value pairs. 

a={"python":"Fees=90000",
"java":"Fees=85000",
"C":"Fees=25000",
"C++":"Fees=30000",
"Tally Prime":"Fees=5000",
"CCC":"Fees=4000"}

print(a)


#Q-2. Write a Python program to access values using keys from a dictionary.

a={"python":"Fees=90000",
"java":"Fees=85000",
"C":"Fees=25000",
"C++":"Fees=30000",
"Tally Prime":"Fees=5000",
"CCC":"Fees=4000"}

print(a["C"])
print(a["C++"])
print(a["CCC"])
print(a["Tally Prime"])
print(a["java"])
print(a["python"])


#==================================================>Lab-7<==============================================================
# ==================================================> Working with Dictionaries<===================================================

#Q-1.Write a Python program to update a value in a dictionary. 

a={"Name":"Rani","Email":"Rani@gmail.com","Phone":"1235456987"}
print(a)
a.update({"Name":"Tisha","Email":"Tisha@gmail.com","Phobne":"1265497784"})
print(a)


#Q-2.Write a Python program to merge two lists into one dictionary using a loop. 

a=["Name","Email","Age"]
b=["Riddhi","Riddhi@gmail.com",20]
c={}

for i in range(len(a)):
    c[a[i]]=b[i]
print(c)


# ----------------------------------------------------->Practical Examples:<--------------------------------------

#Q-1. Write a Python program to update a value at a particular key in a dictionary. 

a={"Name":"Ishika","Email":"Ishika@gmail.com","Phone":"145236987"}
print(a)
a.update({"Name":"Aastha"})
print(a)


#Q-2.Write a Python program to separate keys and values from a dictionary using keys() and values() methods.


a={"Name":"Hency","Email":"Hency@gmail.com","Phone":"1235869","Gradution":"BCA"}
print(a.keys())
print(a.values())
print(a.items())


#Q-3.Write a Python program to convert two lists into one dictionary using a for loop. 

List1=["A","B","C","D"]
List2=[10,20,30,40,50]

result={}
for i in range(len(List1)):
    result[List1[i]]=List2[i]
print(result)


#Q-4.Write a Python program to count how many times each character appears in a string. 

a="My Name Is Tisha"
count=0
for i in a:
    if str(i).isalpha():
        count+=1
print("total character appears in a string:" ,count)



#==================================================>Lab-8<==============================================================
# ==================================================> Functions <=======================================================

#Q-1.Write a Python program to create a function that takes a string as input and prints it.

def person(Name):
    print(Name)

person("MY NAME IS TISHA")    


#Q-2.Write a Python program to create a calculator using functions.

def add(num1,num2):
    return num1+num2

def subtraction(num1,num2):
    return num1-num2

def Multipection(num1,num2):
    return num1*num2

def divide(num1,num2):
    return num1/num2

def Moduls(num1,num2):
    return num1%num2

def Exponentiation(num1,num2):
    return num1**num2

def Floor_division(num1,num2):
    return num1//num2

print("Select Operation:")
print("1. add")
print("2. subtraction")
print("3. Multipection")
print("4. divide")
print("5. Moduls")
print("6. Exponentiation")
print("7. Floor_division")

choice=input("Enter Your Choice:")
num1=float(input("Enetr the value of num1:"))
num2=float(input("Enetr the value of num2:"))

if choice=="1":
    print("Result:",add(num1,num2))
elif choice=="2":
    print("Result:",subtraction(num1,num2))
elif choice=="3":
    print("Result:",Multipection(num1,num2))
elif choice=="4":
    print("Result:",divide(num1,num2))
elif choice=="5":
    print("Result:",Moduls(num1,num2))
elif choice=="6":
    print("Result:",Exponentiation(num1,num2))
elif choice=="7":
    print("Result:",Floor_division(num1,num2))
else:
    print("Sorry! Invalid Choice")


# ----------------------------------------------------->Practical Examples:<--------------------------------------

#Q-1.Write a Python program to print a string using a function. 

def Person_details(Name,Email,Age,Course):
    print(Name,Email,Age,Course)

Person_details("Tisha","T@gmail.com",20,"Python")


#Q-2. Write a Python program to create a parameterized function that takes two arguments and prints their sum.

def Addition(Num1,Num2):
    print(f"Sum Of {Num1} & {Num2}:{Num1+Num2}")

Addition(10,10)


#Q-3.Write a Python program to create a lambda function with one expression.

A=lambda a: a*a
print(A(10))


#Q-4.Write a Python program to create a lambda function with two expressions.

B=lambda a,b:a**b
print(B(5,2))


#==================================================>Lab-9<==============================================================
# ==================================================>Modules<===========================================================

#Q-1.Write a Python program to import the math module and use functions like sqrt(), ceil(), floor(). 

import math

print(math.sqrt(144))
print(math.ceil(11.11))
print(math.floor(10.1))
print(math.pow(5,2))
print(round(10.2))


#Q-2.
# Write a Python program to generate random numbers using the random module.

import random
A=random.randint(10,20)
print(A)


# ----------------------------------------------------->Practical Examples:<--------------------------------------

#Q-1.Write a Python program to demonstrate the use of functions from the math module.


import math

print(math.sqrt(121))
print(math.ceil(55.69))
print(math.floor(8.5))
print(math.pow(10,3))
print(round(25.69))


#Q-2.Write a Python program to generate random numbers between 1 and 100 using the random module.
 
import random

B=random.randint(1,100)
print(B)