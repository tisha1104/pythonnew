#===================================================Lab-1============================================
# Q1.Write a Python program that prints "Hello, World!".

print("Hello, World!")

# Q2.Set up Python on your local machine and write a program to display your name.

name= "Patel Tisha"

print(f"My name is {name}")

#===================================================Lab-2============================================
#Q1.Write a Python program that demonstrates the correct use of indentation, comments, and variables following PEP 8 guidelines.

a=10
b=5
# a=int(input("Enter The Number:-"))
# b=int(input("Enter The Number:-"))
# print(f"a={a}")
# print(f"b={b}")

Addition=(a+b)
print(f"Sum of a+b={Addition}")

Subtraction=(a-b)
print(f"Subtraction of a-b={Subtraction}")

Multiplication=(a*b)
print(f"Multiplication of a*b={Multiplication}")

Division=(a/b)
print(f"Division of a/b={Division}")

Modul=(a%b)
print(f"Moduls of a%b={Modul}")

Exponentiation=(a**b)
print(f"Exponentiation of a**b={Exponentiation}")

Floor_division=(a//b)
print(f"floor_division of a//b={Floor_division}")


#===================================================Lab-3============================================
#Q1.Write a Python program to demonstrate the creation of variables and different data types. 

# a=10  int
# print(a)

# b= "Tisha" string
# print(b)

# c=15.50 float
# print(c)

# Subject=["Python","c","c++"] list
# print(Subject)

# for i in range(5): range
#     print(b)


#Q2.Practical Example 1: How does the Python code structure work? 

a=10
print(a)

#Q3.Practical Example 2: How to create variables in Python? 

Name= "Ishika"
age=21
email="ishika29@gmail.com"

print(Name,age,email)


#Q4.Practical Example 3: How to take user input using the input() function.

Name=input("Enter the name:")
print(Name)


#Q5.Practical Example 4: How to check the type of a variable dynamically using type(). 

a=11
b=5.96
Name= "Rani"
c=["Mango","Banana","Charry"]

print(type(a))
print(type(b))
print(type(Name))
print(type(c))


#===================================================Lab-4============================================
#Q1.Practical Example 5: Write a Python program to find greater and less than a number using if_else. 

Number1=int(input("Enter the Number1 "))
Number2=int(input("Enter the Number2 "))

if Number1>Number2:
    print(f"{Number1} is Greater than {Number2}") 
else:
    print(f"{Number2} is Greater than {Number1}") 


#Q2.Practical Example 6: Write a Python program to check if a number is prime using if_else.

Number=int(input("Enter The Number:"))
i=1
c=0

if Number<=1:
    print("Number is Not Prime")
else:
    while i<=Number:
        if Number%i==0:
            c+=1
        i+=1
    if c==2:
        print("Number is Prime")
    else:
        print("Number is Not Prime")


#Q3.Practical Example 7: Write a Python program to calculate grades based on percentage using if-else ladder.

persantage=float(input("Enter the Marks:-"))

if persantage>=91 and persantage<=100:
    print("your grade is A")
elif persantage>=71 and persantage<=90:
    print("your grade is B")
elif persantage>=51 and persantage<=70:
    print("your grade is C")
elif persantage>=35 and persantage<=50:
     print("your grade is D")
else:
    print("fail")


#Q4.Practical Example 8: Write a Python program to check if a person is eligible to donate blood using a nested if. 

age= int(input("Enter your age:-"))

if age>18:
    print("You can go to donate")
    if age>=18:
        print("You are eligible to donate blood")
else:
    print("You are not eligible to donate blood")


#===================================================Lab-5============================================
#Q1.Practical Example 1: Write a Python program to print each fruit in a list using a simple for loop. List1 = ['apple', 'banana', 'mango'].

List1 = ['apple', 'banana', 'mango']
for i in range(1):
    print(List1)


#Q2.Practical Example 2: Write a Python program to find the length of each string in List1. 

List1 = ['apple', 'banana', 'mango']
for word in List1:
    print(f"length of {word} is {len(word)}")


#Q3.Practical Example 3: Write a Python program to find a specific string in the list using a simple for loop and if condition.

fruit= ['apple', 'banana', 'mango']
search=input("Enter Your String:-")

for i in fruit:
    if i==search:
        print("string in the list")
        break
    else:
        print("string is not in the list")


#Q4.Practical Example 4: Print this pattern using nested for loop: 

for i in range (5):
        for j in range(i+1):
            print("*",end=" ")
        print()



for i in range(5):
    print("*"*(i+1))


#===================================================Lab-8============================================
#Q1.Practical Example: 1) Write a Python program to skip 'banana' in a list using the continue statement. List1 = ['apple', 'banana', 'mango'] 

List1 = ['apple', 'banana', 'mango']

for i in List1:
    if i=="banana":
        continue
    print(i)
     
          
#Q2.Practical Example: 2) Write a Python program to stop the loop once 'banana' is found using the break statement.
 
List1 = ['apple', 'banana', 'mango']

for i in List1:
    if i=="banana":
        break
    print(i)


#===================================================Lab-9============================================
#Q1.Write a Python program to demonstrate string slicing. 

str="Hello Python!"

print(str[1:])
print(str[:5])
print(str[5:9])
print(str[-5:-2])
print(str[::-1])


#Q2.Write a Python program that manipulates and prints strings using various string methods.

st= "my name is tisha"
print(len(st))

st= "MY NAME IS TISHA"
print(str.lower(st))

st= "my name is tisha"
print(str.upper(st))

st= "my name is tisha"
print(str.capitalize(st))

st= "my name is tisha"
print(str.title(st))

st= "  my name is tisha   "
print(st)
print(st.strip())

st= "my name is tisha"
print(st.replace('i','r',1))

st= "my name is tisha"
print(st.find("tisha"))

st= "my name is tisha"
print(st.startswith("M"))

st= "my name is tisha"
print(st.endswith("a"))

st= "my name is tisha"
print(st.split(" ",2))

print("XYZ".join("abc"))

print("Tisha".isalpha())

print("2004".isdigit())

print("Tisha2004".isalnum())

print("Rani".zfill(50))

print("Rani".center(50,"*"))