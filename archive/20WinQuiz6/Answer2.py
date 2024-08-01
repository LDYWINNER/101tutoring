
class Package:
    def __init__(self, sender, recipient, cost):
        self.sender = sender
        self.recipient = recipient
        self.cost = cost

    def __repr__(self):
        return 'recipient: ' + self.recipient + ' and cost: ' + str(self.cost)

a = Package('Abe', 'Byung', 20)
b = Package('Chris', 'Dana', 10)
c = Package('Dongyeob', 'Chorong', 15)
d = Package('Tim', 'Hasung', 25)

boxes = [a, b, c, d]
#print(boxes)

total = 0
for box in boxes:
    total += box.cost
print(total)

for box in boxes:
    print(box)
