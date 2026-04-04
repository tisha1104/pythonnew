# Check whether a number is even or odd
num=int(input("Enter The Number:- "))
if num%2==0:
    print(f"{num} is even number")
else:
    print(f"{num} is odd number")

# Check number type
num=int(input("Enter The Number:- "))

if num>0:
    print(f"{num} is Positive Number")
elif num<0:
    print(f"{num} is Negitive Number")
else:
    print(f"{num} is Zero")

# Find largest among 3 numbers
a=int(input("Enter The Number :- "))
b=int(input("Enter The Number :- "))
c=int(input("Enter The Number :- "))

if a>=b and a>=c:
    print(f"{a} is Largest number")
elif b>=a and b>=c:
    print(f"{b} is Largest number")
else:
    print(f"{c} is Largest number")

# Create a single program that does ALL:
num=int(input("Enter the number:- "))
# if num%2==0:
#     print(f"{num} is even number")
# else:
#     print(f"{num} is odd number")

# if num>0:
#     print(f"{num} is Positive Number")
# elif num<0:
#     print(f"{num} is Negitive Number")
# else:
#     print(f"{num} is Zero")
if num % 2 == 0:
    print("Even")
else:
    print("Odd")

if num >= 0:
    if num == 0:
        print("Zero")
    else:
        print("Positive")
else:
    print("Negative")