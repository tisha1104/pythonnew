# ==================================================>Lab-1<==============================================================
# ==================================================>Accessing List<=====================================================

#Write a Python program to create a list with elements of multiple data types (integers, strings, floats, etc.).

l=["Tisha","Rani",10,20,30,40,50,10.5,11.11,12.58,"5x","11y"]
# print(l)

# for i in l:
#     print(i)

# for i in range(len(l)):
#     print(l[i])


#Write a Python program to access elements at different index positions. 

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

#Write a Python program to add elements to a list using insert() and append(). 

# list1=["Python","java","C"]
# list1.insert(1,"C++")
# print(list1)
# list1.append("SQL")
# print(list1)


#Write a Python program to remove elements from a list using pop() and remove(). 

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

#Write a Python program to iterate over a list using a for loop. 

# fruit=["Mango","Apple","Banana","Charry","Dragon Fruit","Lichi"]

# for fruit in fruit:
#     print(fruit)


#Write a Python program to sort a list using both sort() and sorted(). 

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

#Write a Python program to create a tuple with multiple data types.

# t=(10,20,30,40,50,50,60,710,"Tisha","Rani",False,True,11.11,10.96,8.1,"5J","10X","11Y")
# print(t)


#Write a Python program to concatenate two tuples. 

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
