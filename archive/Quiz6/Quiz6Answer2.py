# CSE 101 DongYoon Lee
# Email: DongYoon.Lee.1@stonybrook.edu

class Package:
    def __init__(self, sender, recipient, cost):
        self.sender = sender
        self.recipient = recipient
        self.cost = cost

    def __repr__(self):
        return str(self.recipient) + str(self.cost)

#step 1
a = Package('Abe', 'Byung', '20')
b = Package('Chris', 'Dana', '10')
c = Package('Dongyeob', 'Chorong', '15')
d = Package('Tim', 'Hasung', '25')
boxes = [a, b, c, d]

#step2
total = 0
for alphabet in boxes:
    total += int(alphabet.cost)
print(total)

#step 3
for box in boxes:
    print(box)