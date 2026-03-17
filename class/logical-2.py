print("========palidrom==========")
n=12345654321
temp=n
sum=0

while n!=0:
    rem=n%10
    sum=sum*10+rem
    n=n//10

if (sum==temp):
    print("number is palidrom")
else:
    print("number is not palidrom")

print("=============Fibonacci==========")
n=int(input("Enter the number"))
a=0
b=1
for i in range(n):
    print(a,end=" ")
    c=a+b
    a=b
    b=c


print("=============Fibonacci Using Recursion==========")


def fibonacci(n):
    if n==0:
        return 0
    elif n==1:
        return 1
    else:
        return fibonacci(n-1)+fibonacci(n-2)
    
num=input("enter the number")
for i in range(n):
    print(fibonacci(i))

print("=============Factorial==========")

n=int(input("Enter the number"))
fact=1

while n!=0:
    fact=n*fact
    n-=1
print(fact)

print("==============Prime number=========")

n=int(input("Enter the Number"))
flag=0

for i in range(2,n):
    if n%i==0:
        flag=1
        break
if flag==0:
    print("number is prime")
else:
    print("numberis not prime")

print("=============Armstrong==========")

num=int(input("Enter The Number"))
temp=num
sum=0

while num!=0:
    rem=num%10
    sum+=rem**3
    num=num//10
if(sum==temp):
    print("number is Armstrong")
else:
    print("number is not Armstrong")


print("=============Armstrong==========")

for i in range(100,1000):
    num=i
    temp=num
    sum=0
    while num!=0:
        rem=num%10
        sum+=rem**3
        num=num//10
    if(sum==temp):
        print(f"number {i} is Armstrong")
    else:
        print("number is not Armstrong")
        # pass

# write a program to count the vowels and consonent
print("=============count the vowels and consonent==========")

sentence=input("Enter The Sentence :- ")

volwes=['a','e','i','o','u']

present_volwes=[]
present_consonent=[]

volwes_count=0
consonent_count=0

sentence=sentence.lower()

for ch in sentence:
    if ch.isalpha():
        if ch in volwes:
            volwes_count+=1

            if ch not in present_volwes:
                present_volwes.append(ch)
            
        else:
            consonent_count+=1

            if ch not in present_consonent:
                present_consonent.append(ch)

print("Present Volwes :- ",present_volwes)
print("Total number of Volwes :- ",volwes_count)

print("Present consonent :- ",present_consonent)
print("Total number of consonent :- ",consonent_count)


print("=============swapping Pythonic Method==========")


a = int(input("Enter a: "))
b = int(input("Enter b: "))

a, b = b, a

print("a:", a)
print("b:", b)

#swapping of two number without using theired varibale
print("=============swapping Method==========")

a=int(input("Enter The a :- "))
b=int(input("Enter The b :- "))

a=a+b
b=a-b
a=a-b
print("After swapping value of a:", a)
print("After swapping value of b:", b) 


print("=============Reverse a string using slicing==========")

string=input("Enter The String :- ")
reverse=string[::-1]
print("Reversed String :- ",reverse)


print("=============Reverse a string without using slicing==========")

string=input("Enter The String :- ")
reverse=""
for i in string:
    reverse=i+reverse
print(reverse)




print("=============remove duplicate characters from a string in Python==========")

string=input("Enter The String :- ")
result=""
for i in string:
    if i not in result:
        result=result+i
print("String after removing duplicates:", result)




print("=============Find Second Largest Number==========")

numbers=[1,2,3,4,5,6,14,85,96,101,111,178]
numbers.sort()
print(numbers[-2])

print("=============Check Anagram==========")

s1=input("enter your word :- ")
s2=input("enter your word :- ")

if sorted(s1)== sorted(s2):
    print("Anagram")
else:
    print("Not Anagram")


print("Write program to manuplate a version string")

# version="1.0.0"
version=input("Enetr Your version")
a,b,c=map(int,version.split("."))
c+=1

if c==100:
    c=0
    b+=1

if b==100:
    b=0
    a+=1

print(a,".",b,".",c,sep="")


print("Write program to decrement a version string")

version="1.0.0"
# version=input("Enetr Your version")
a,b,c=map(int,version.split("."))
c-=1

if c<0:
    c=99
    b-=1

if b<0:
    b=99
    a-=1

print(a,".",b,".",c,sep="")