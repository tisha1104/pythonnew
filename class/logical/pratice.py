# n=125
# temp=n
# sum=0
# while n!=0:
#     rem=n%10
#     sum=sum*10+rem
#     n=n//10
# if (sum==temp):
#     print("number is palidrom")
# else:
#     print("number is not palidrom")

# n=int(input("enter the number "))
# a=0
# b=1
# for i in range(n):
#     print(a,end=" ")
#     c=a+b
#     a=b
#     b=c

def fibonacci(n):
    if n==0:
        return 0
    elif n==1:
        return 1
    else:
        return fibonacci(n-1)+fibonacci(n-2)
    
num=int(input("Enter the number "))
for i in range(num):
    print(fibonacci(i))

n=int(input("Enter The Number:- "))
fact=1
while n!=0:
    fact=n*fact
    n-=1
print(fact)