l=[10,20,30,40,50,60]

def square(a):
    return a*a

s=[]
for i in l:
    k=square(i)
    s.append(k)
print(s)

s= map(square,l)
s=map(lambda a:a*a,l)
print(list(s))

l=[1,2,3,4,5,6,7,8,9]

def oddnumber(a):
    if a%2!=0:
        return True
    else:
        return False
    
s=[]
for i in l:
    k =oddnumber(i)
    if k:
        s.append(i)

print(s)

s=filter(oddnumber,l)
s=filter(lambda a: a%2==0,l)
print(list(s))

from functools import reduce

l=[1,2,3,4,5,6,7,8,9]

def max(a,b):
    if a>b:
        return a
    else:
        return b
    
k=reduce(sum,l)
k=reduce(lambda a,b:a+b,l)
k=reduce(max,l)
k=reduce(lambda a,b: a if a>b else b,l)
print(k)

