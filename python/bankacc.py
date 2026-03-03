class Bank:
    Bank_name="UNION BANK"
    def __init__(self,name,balance):
        self.holder=name
        self.balance=balance
    @classmethod
    def change_bankname(cls,newname):
        cls.Bank_name = newname
    def deposit(self,amount):
        self.balance+=amount
    @staticmethod
    def validate(amount):
        return amount>0
b1= Bank("Gopi",10000000000)
b1.change_bankname("UNION BANK")
Bank.change_bankname("UNION BANK")
b1.deposit(100000000000)
print(b1.validate(1000))
print(Bank.validate(b1.balance))