from abc import *

class SBI_Bank(ABC):
    @abstractmethod
    def Balance(self):
        ...

    @abstractmethod
    def Deposit(self,amount):
        ...

    @abstractmethod
    def Withdrawal(self,amount):
        ...
class user_1 (SBI_Bank):
    def __init__(self,acc_holder_name,bal):
        self.name = acc_holder_name
        self.bal = bal

    def Balance(self):
        print(self.name , self.bal)


    def Deposit(self,amount):
        self.bal += amount
        print(amount)

    def Withdrawal(self,amount):
        self.bal -= amount
        print(amount)
b = user_1("Kunal", 45000)
# b.bal = 455
b.Balance()
b.Deposit(34000)
b.Withdrawal(34)