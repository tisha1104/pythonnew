from functools import reduce

l=[16,202,250,369,14,58,30,58,20,147,11]

def min(a,b):
    if a<b:
        return a
    else:
        return b
    
k=reduce(min,l)
k=reduce(lambda a,b: a if a<b else b,l)
print(k)
    
l=[10,20,30,40,50,60,70,80,90,100]
def avg(numbers):
    b=sum(numbers)/len(numbers)
    print(b)

# avg(l)
k=reduce(avg,l)
print(k)