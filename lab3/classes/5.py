class Account:
    def __init__(self, owner, balance):
        self.owner = owner
        self.balance = balance
    def deposit(self, a):
        self.balance = self.balance + a

    def withdraw(self, b):
        if self.balance >= b:
            self.balance = self.balance - b
            return "Ok"
        else:
            return "Stop!!!"
    def show_balance(self):
        print(self.balance)

Anyu = Account('Alua', 50)
Anyu.deposit(100)
print(Anyu.withdraw(151))
Anyu.show_balance()

Anyu.deposit(2000)
print(Anyu.withdraw(150))
Anyu.show_balance()



