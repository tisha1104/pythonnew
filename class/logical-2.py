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
        # print("number is not Armstrong")
        pass
