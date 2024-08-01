
class Card:
    suit_sym = {3: '\u2660', 2: '\u2665', 1: '\u2666', 0: '\u2663'}
    rank_sym = {0: '2', 1: '3', 2: '4', 3: '5', 4: '6', 5: '7', 6: '8', 7: '9', 8: '10', 9: 'J', 10: 'Q', 11: 'K', 12: 'A'}

    suit_num = dict(zip(suit_sym.values(), suit_sym.keys()))
    rank_num = dict(zip(rank_sym.values(), rank_sym.keys()))

    def __init__(self, arg1, arg2 = None):
        if type(arg1) == int:
            if arg1 in range(0, 52):
                self.id = arg1
            else:
                raise Exception('Card number must be between 0 and 51')

        elif arg1 in Card.rank_num and arg2 in Card.suit_num:
            self.id = Card.rank_num[arg1] + Card.suit_num[arg2] * 13

        else:
            raise Exception("Expected Card(n) or Card('rank', 'suit')")

    def __repr__(self):
        return Card.rank_sym[self.rank()] + Card.suit_sym[self.suit()]

    def rank(self):
        return self.id % 13

    def suit(self):
        return self.id // 13

print(Card(32))

a = Card(23)
print(a.suit_num)
print(Card.suit_sym)
