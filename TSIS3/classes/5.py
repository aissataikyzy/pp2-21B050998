class Account:
    def __init__(self, owner, balance):
        self.owner = owner
        self.balance = balance

    def deposite(self, money):
        self.balance += money
        print(self.balance)

    def withdraw(self, money):
        if(self.balance >= money and self.balance > 0):
            self.balance -= money
        else:
            print("Stop being horny and give me your mora")
        print(self.balance)

money = int(input())
balance = int(input())
owner = "Akbota"

a = Account(owner, balance)
a.deposite(money)
money2 = int(input())
a.withdraw(money2)
