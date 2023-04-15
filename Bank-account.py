# Bank Account
class Bank:
    def __init__(self):
        self.balance = 0
        print("The Account is created")
    def deposit(self):
        amount = float(input("Enter the amount you want to deposit "))
        self.balance = self.balance + amount
        print("Deposit is successful")
    def withdraw(self):
        amount = float(input("Enter the amount you want to withdraw "))
        if (self.balance>=amount):
            self.balance = self.balance - amount
            print("The withdraw is successful")
        else:
            print("Insuficient balance")
    def final(self):
        print("The amount of money in the account is %f" % self.balance)

acc = Bank()
acc.deposit()
acc.withdraw()
acc.final()
