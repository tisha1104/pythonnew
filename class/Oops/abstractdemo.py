from abc import ABC, abstractmethod

class Account(ABC):
    
    balance=0
    @abstractmethod
    def deposite(self,amt):
        pass

    @abstractmethod
    def Withdrow(self,amt):
        pass
    
    def getbalance(self):
        print("Current balaance is : ",self.balance)

class Saving(Account):
    
    def deposite(self, amt):
        self.balance+=amt

    def Withdrow(self, amt):
        if amt>self.balance:
            print("Insufficeinet amount")
        else:
            self.balance-=amt

class Loan(Account):
    def deposite(self, amt):
        self.balance-=amt

    def Withdrow(self, amt):
        self.balance+=amt

s=Saving()
s.getbalance()
s.deposite(5000)
s.deposite(3000)
s.getbalance()
s.Withdrow(5000)
s.getbalance()