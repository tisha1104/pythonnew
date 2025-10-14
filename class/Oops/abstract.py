from abc import ABC, abstractmethod

class Demo(ABC):

    @abstractmethod
    def test(self):
        pass

class DemoImp(Demo):

    def test(self):
        print("test calling....")

# d=Demo()
# d.test()

d=DemoImp()
d.test()


