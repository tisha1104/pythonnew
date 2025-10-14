class sample:
    id =11
    name="Rani"

    def display(self):
        return f"MY Name is {self.name} and id is {self.id}"
    
class Demo:
    s = sample()
    def show(self):
        return "Show Calling..."
    
d=Demo()
d.s.display()
print(d.s.display())