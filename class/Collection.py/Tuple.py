t=(10,20,30,40,50,50,60,710,"ABC",True,11.11)
t1=tuple((10,20,30,40,50,550,55.55))
t2=(11,)
print(t)
print(t1)
print(type(t))
print(type(t1))
print(type(t2))
print(len(t))

l=[10,20,30]
l1=[10]
print(type(l))
print(type(l1))

print(t[1])
print(t[1:5])
print(t[-1])
print(t[::-1])

l=list(t)
l.append("Tisha")
print(type(l))
print(tuple(l))
print(type(t))
print(t)
print(l)

t1=(10,20,30,40,50)
(a,b,*c,d)=t1
print(c)
print(b)

print(t1*2)