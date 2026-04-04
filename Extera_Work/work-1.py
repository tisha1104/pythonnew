name=input("Enter Your Name :- ")
city=input("Enter Your City :- ")
fav_num=int(input("Enter Your Number :- "))
print(f"My name is {name}. I live in {city}. My Favorite number is {fav_num}.")
print("========================================================================")
x=10
y=3.5
z="Hello"
print(type(x))
print(type(y))
print(type(z))

print(x+y)
print(x*y)
print(x*z)
print(z*x)
print("========================================================================")
name=input("Enter Your Name :- ")
age=int(input("Enter Your Age :- "))
print("Hello",name,"You are",age," Years old")

print("=================== Calculator Gate ===========================")
num1=float(input("Enter Number :- "))
num2=float(input("Enter Number :- "))

add=(num1+num2)
print("addition of two number:- ",add)

sub=(num1-num2)
print("subtraction of two number:- ",sub)

mul=(num1*num2)
print("Multiplication of two number:- ",mul)

div=(num1/num2)
if num2!=0:
    print("Division of two number :- ",div)
else:
    print("Cannot divide by zero")

print("=================Find largest of 2 numbers=============")
a=10
b=20

# if a>b:
#     print(a)
# else:
#     print(b)
if a > b:
    print(a, "is greater")
elif b > a:
    print(b, "is greater")
else:
    print("Both numbers are equal")

