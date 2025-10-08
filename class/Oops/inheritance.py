class pen:
    price=100
    color="Red"
    company="Cello"

    def display(self):
        print(self.price,self.color,self.company)

class Notebook(pen):
    Pages=100

    def show(self):
        self.price=50
        print(self.price,self.color,self.company,self.Pages)

# class Bag(Notebook):-Multilevel
# class Bag(pen):-Hierarchical
# class Bag(pen,Notebook):-Multiple

p=pen()
p.display()
n=Notebook()
n.show()


class clg:

    def __init__(self,id,name,email):
        self.id=id
        self.name=name
        self.email=email
    
    def display(self):
        print(self.id,self.name,self.email)

class Student(clg):

    def __init__(self, id, name, email):
        super().__init__(id, name, email)

    def show(self):
        print(self.id,self.name,self.email)

c=clg(11,"Tisha","T@gmail.com")
c.display()

s=Student(11,"Rani","R@gmail.com")
s.show()
s.display()


class Animal:

    def __init__(self,name):
        self.name=name

    def sleep(self):
        print("Animal is sleeping")

    def eat(self):
        print("Animal is eating")

class Dog(Animal):
    
    def __init__(self, name,breed):
        super().__init__(name)
        self.breed=breed

    def bark(self):
        print(f"The Dog {self.name} of breed {self.breed} is barking!")

d= Dog("Tommy","green shepherd")
d.bark()
d.sleep()
d.eat()

class A:
    def __init__(self):
        print("A Construcor Calling....")

class B(A):
    def __init__(self):
        super().__init__()
        print("B Construcor Calling....")

b=B()