s={"A","B","C","D","A",100,1,True,0,False}
print(s)

for x in s:
    print(s)

print(type(s))

print("A" in s)

s.add("XYZ")
s.update({"P","Q"})
print(s)

s.remove("A")
s.discard("AB")
s.pop()
s.clear()
del s
print(s)

a={1,2,3,4,5}
b={4,5,6,7,8,True}
print(a)
print(b)

c= a.union(b)
a.update(b)
c=a|b
print(c)

c = a.intersection(b)
c = a&b
a.intersection_update(b)
print(a)

c=a.difference(b)
c = a-b
a.difference_update(b)
print(a)

c = a.symmetric_difference(b)
c= a^b
a.symmetric_difference_update(b)
print(a)


k = {10,20,30,40,50}
j = {100,200}

print(j.issubset(k))
print(k.issuperset(j))

print(j.isdisjoint(k))