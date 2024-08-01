
# Create the Account class here
class Account:
    def __init__(self, name, balance):
        self.name = name
        self.balance = balance

    def __repr__(self):
        return self.name + str(self.balance)

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        if amount > self.balance:
            print('Not enough funds')
            pass
        else:
            self.balance -= amount



a = Account("Alice", 100)
print("Initial account:", a)

a.deposit(50)
print("After deposit 50:", a)

a.withdraw(120)
print("After withdraw 120:", a)

a.withdraw(60)
print("After withdraw 60:", a)