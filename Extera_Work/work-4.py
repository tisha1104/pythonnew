# counts digits in a number
# num=input("enter the number:- ")
# print(len(num))
# num = int(input("Enter number: "))
# count = 0

# num = abs(num)   # handle negative numbers

# while num > 0:
#     count += 1
#     num //= 10
# print(count)
# Create function intro()
# name=input("enter your name:- ")
# age=input("enter your age:- ")
# city=input("enter your city:- ")
def intro(name,age,city):
    print(f"My Name is {name}. I am {age} Year Old. I live in {city} city.")

intro("Tisha",20,"Surat")

# Print sum
def add(a,b):
    c=a+b
    print(c)
add(10,50)


# square(n) → return square

def square(a):
    return a*a

result=square(2)
print(result)

# Modular Calculator
a=int(input("Enter the a:- "))
b=int(input("Enter the b:- "))

def add(a,b):
    return a+b

def sub(a,b):
    return a-b

def mul(a,b):
    return a*b

def div(a,b):
    try:
        return a/b
    except ZeroDivisionError:
        print("division by Zero")

print("Modular Calculator")
print(add(a,b))
print(sub(a,b))
print(mul(a,b))
print(div(a,b))
