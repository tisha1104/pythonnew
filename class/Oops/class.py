class pen:
    price=10
    company='cello'
    color='red'

    def to_write(self):
        print("Write Method Calling...")
        print(self.price,self.color,self.company)

p=pen()
p.to_write()

p1=pen()
p1.price=100
p1.to_write()

p2=pen()
p2.to_write()


class student:
    id=101
    Name='Rani'
    email='Rani@gmail.comn'
    Phone=852369741

    def display(self):
        print(self.id)
        print(self.Name)
        print(self.email)
        print(self.Phone)

Records=student()
Records.display()