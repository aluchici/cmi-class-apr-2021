# loans, saving account, debit account
# metoda pt a crea un obiect nou

class Account:

    def __init__(self, amount):
        self.amount = amount
    
acc1 = Account(10000)
print(acc1.amount)

class Loan(Account):
    pass

class SavingAccount(Account):
    rate = 0.1

    def __init__(self, amount, exp_date):
        super(SavingAccount, self).__init__(amount)
        self.exp_date = exp_date
    
    def deposit(self, value):
        self.amount = self.amount + value

sav1 = SavingAccount(20000, '122121')
print(sav1.amount)
print(sav1.exp_date)

sav1.deposit(300000)
print(sav1.amount)