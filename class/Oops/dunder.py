# The class Demo defines a class with attributes id and name,and a method __str__ that returns a formatted
# string with the values of id and name.
class Demo:
    id=11
    name="Rani"
    def __str__(self):
        return f"my name is {self.name} and id is {self.id}"
    
d=Demo()
print(d)


# The commented code defines a class named 'Calc' with three special methods:


class Calc:
    def __init__(self,a,b):
        self.a=a
        self.b=b

    def __add__(self,obj):
        return self.a+obj.a,self.b+obj.b
    
    def __eq__(self, obj):
        return self.a==obj.a and self.b==obj.b
    
c =Calc(11,12)
c1 =Calc(10,2)

k = c+c1
print(k)
print(c==c1)



# The class Demo allow for setting and getting Values at specific indices in a list stored as an 
# attribute.

class Demo:

    def __init__(self,item):
        self.item= item

    def __setitem__(self,index,value):
        self.item[index]=value

    def __getitem__(self,index):
        return self.item[index]
    
d =Demo([10,20,30,40,50,60,70,80,90])
d[3]=100
print(d.item)
print(d[3])