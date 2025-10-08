from multipledispatch import dispatch
class calc:
    @dispatch(int,int)
    def add(self,a,b):
        print(a+b)

    @dispatch(int,int,int)
    def add(self,a,b,c):
        print(a+b+c)

    # def add(self,*a):
    #     sum=0
    #     for i in a:
    #         sum+=i
    #         print(sum)

c=calc()
c.add(10,11)
c.add(10,11,20)


class A:
    def disp(self):
        print("A disp Calling....")

class B(A):
    def disp(self):
        print("B disp Calling....")

b=B()
b.disp()