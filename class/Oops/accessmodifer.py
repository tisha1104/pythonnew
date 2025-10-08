class Demo:

    __name="XYZ"
    email="XYZ@gmail.com"

    def show(self):
        print(self.__name,self.email)

d=Demo()
print(dir(d))
d._Demo__name="abc"
d.show()