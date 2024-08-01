class Card:

    suits = {3: '\u2660', 2:'\u2665', 1: '\u2666', 0: '\u2663'}
    ranks = {0: '2', 1: '3', 2: '4', 3: '5', 4: '6', 5: '7', 6: '8', 7: '9', 8: '10', 9: 'J', 10: 'Q', 11: 'K', 12: 'A'}

    def __init__(self, n):
        self._id = n

    def rank(self):
        return self._id % 13

    def suit(self):
        return self._id // 13

    def __repr__(self):
        return Card.ranks[self.rank()] + Card.suits[self.suit()]

    def __eq__(self, other):
        return self._id == other._id

    def __lt__(self, other):
        return self._id < other._id

def new_deck():
    return [Card(i) for i in range(52)]