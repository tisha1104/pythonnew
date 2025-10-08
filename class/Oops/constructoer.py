# class student:

#     clg="DSC"
#     def __init__(self,id,name,email):
#         self.name=name
#         self.id=id
#         self.email=email

#     def display(self):
#         print("Runing display...")
#         print(self.id,self.name,self.email)

#     @classmethod
#     def sample(self):
#         print(self.clg)
#         print("sample calling...")

#     @staticmethod
#     def run():
#         print("run calling...")

# student.clg='ABC'
# student.sample()

# student.run()

# s=student(10,"Rani","Rani@gmail.com")
# s.display()

class demo:
    id=11
    def display(self):
        print("display calling")

    @classmethod
    def sample(self):
        print("Sample Calling....",self.id)

    @staticmethod
    def util():
        print("Static Calling...")

d=demo()
d.display()
demo.sample()
demo.util()


class std:

    def __init__(self,*a):
        print("Hello",a)

    def __init_subclass__(self,a,b):
        print("Hello",a,b)

    def show(self):
        print("Show Calling....")

s=std(10)
s.show()