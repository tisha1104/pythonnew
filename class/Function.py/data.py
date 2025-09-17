def hello():
    print("Hello World")

hello()

def square(a):
    print(a*a)

square(1000)

def add(a,b):
    print(a+b)

add(10,50)

def add(a,b):
    return a+b

def square(a):
    return a*a

c=add(5,5)
k=square(c)
print(k)

def person(id=0,name=0,email=0):
    print(id,name,email)

person(10,name="tisha@gmail.com")

def add(*a):
    print(a)

add(10,20,30,410,50,8566)

def person(**a):
    print(a)

person(name="Tisha",email="t@gmail.com")

a=lambda a,b : a+b
b=lambda a: a*a

print(a(20,20))
print(b(60))