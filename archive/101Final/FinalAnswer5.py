# CSE 101 DongYoon Lee
# Email: DongYoon.Lee.1@stonybrook.edu

# Create the Account class here

class Account:
    def __init__(self, name, balance):
        self._name = name
        self._balance = balance

    def __repr__(self):
        return '(' + self._name + ',' + str(self._balance) + ')'

    def deposit(self, amount):
        self._amount = amount
        return '(' + self._name + ',' + str(int(self._balance) + int(self._amount)) + ')'

    def withdraw(self, amounts):
        self._amounts = amounts
        if self._amounts > self._balance:
            print("Not enough funds")
            return '(' + self._name + ',' + str(self._balance) + ')'
        else:
            return '(' + self._name + ',' + str(self._balance - self._amounts) + ')'


a = Account("Alice", 100)
print("Initial account:", a)

a.deposit(50)
print("After deposit 50:", a)

a.withdraw(120)
print("After withdraw 120:", a)

a.withdraw(60)
print("After withdraw 60:", a)

