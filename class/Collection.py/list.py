# l=[10,20,30,40,50,50,11.11,"Hello",True,52.86,11,False]
# l1=list((22,23,25,14,145,55,11.15))
# print(l)
# print(len(l))
# print(l1)
# print(type(l))
# print(type(l1))
# print(len(l1))

l=["Tisha","Hency","Aastha","Ishika","Prinshu"]
# print(l[3])
# print(l[1:3])
# print(l[-1])
# print(l[::-1])
print(l[::1])

# l[1]="Rani"
# print(l)
# l[1:3]=["A"]

# l.insert(0,"Rani")
# l.append("Rani")
# print(l)

# k=["T","11","Hello"]
# l.extend(k)
# print(l)

# l.remove("Hency")
# l.pop(1)
# l.pop()
# l.clear()
# del l
# print(l)

# for i in (l):
#     print(i)

# for i in range(len(l)):
#     print(l[i])

# i=0
# while i<len(l):
#     print(l[i])
#     i+=1

# k=[]

# for i in l:
#     if'e' in i:
#         k.append(i)
# print(k)

# k=[i for i in l if "e" in i]
# k=[i for i in l if i.startswith('T')]
# k=["A" for i in l]
# print(k)

# l.sort()
# l.sort(reverse=True)
# l.reverse()
# print(l)

# k=sorted(l)
# print(k)

# k=l.copy()
# k=list(l)
# k=l[:]
# k=l
# print(k)

# a=[10,20,30,40,50,50]
# b=[100,200,300,400]

# c=a+b
# print(c)

# a.extend(b)
# print(a)

# print(a.count(50))

# print(a.index(40))

l=["tisha","red","yellow",1,11,2,True]
print(l[0])
print(l[2:5])
l[0]="black"
print(l)
print(len(l))
l.insert(0,"green")
print(l)
l.append("White")
print(l)
l2=[5,2,9,1]
l2.extend(l)
print(l2)
l.reverse()
print(l)
# l2.sort()
# print(l2)
l3=[5,10,10,2,9,1,8,10,15,10]
l3.sort()
print(l3)
l3.sort(reverse=True)
print(l3)
print(l3.count(10))
print(l3.index(10))
# l4=l3.copy()
# l4=l3
l4=l3[:]
# l4=list(l3)
print(l4)
l4.remove(15)
print(l4)
l.pop(1)
print(l)
l.clear()
print(l)
# del l()
list=["a","b","c"]
list2=[1,2,3,4]
list3=list+list2
print(list3)
for i in list:
    print(i)
t=("red",)
print(type(t))
t1=(1,2,3,4,5,6,788,98,9)
l11=list(t1)
