class InsufficentAmountException(Exception):
    def __init__(self, msg):
        super().__init__(msg)

class Bank:

    balance=0

    def check_balance(self):
        print("Cureent balance is :",self.balance)

    def deposite(self,amt):
        self.balance+=amt

    def withdrow(self,amt):
        if amt>self.balance:
            raise InsufficentAmountException(f"you need more {amt-self.balance} in your account to withdrow")
        else:
            self.balance-=amt

b=Bank()
b.check_balance()
b.deposite(5000)
b.deposite(2000)
b.check_balance()
try:
    b.withdrow(20000)
except Exception as e:
    print(e)
b.check_balance()