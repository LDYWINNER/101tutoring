# CSE 101 DongYoon Lee
# Email: DongYoon.Lee.1@stonybrook.edu

class Card:
    """These are class variables"""
    # clubs, diamonds, hearts, spades
    suit_sym = {0: '\u2663', 1: '\u2666', 2: '\u2665', 3: '\u2660'}
    rank_sym = {0: '2', 1: '3', 2: '4', 3: '5', 4: '6', 5: '7', 6: '8',
                7: '9', 8: '10', 9: 'J', 10: 'Q', 11: 'K', 12: 'A'}

    """These are instance variables:
    _id (suit and rank combined into a single integer)
    """

    def __init__(self, n):
        if n in range(52):
            self._id = n
        else:
            raise Exception('Card number must be in the range 0-51.')

    def suit(self):
        return self._id // 13

    def rank(self):
        return self._id % 13

    def __repr__(self):
        return Card.rank_sym[self.rank()] + Card.suit_sym[self.suit()]

    def __lt__(self, other):
        return self._id < other._id

    def __eq__(self, other):
        return self._id == other._id

def new_deck():
    return [Card(i) for i in range(52)]


def poker_hand(cards):
    same_rank = []
    same_suit = []
    for card in cards:
        same_rank.append(card.rank())
        same_suit.append(card.suit())
    #print(same_rank)
    #print(same_suit)
    for i in range(len(same_rank)):
        if same_rank.count(same_rank[i]) == 4:
            return('Four of a kind')

    for k in range(len(same_suit)):
        if same_suit.count(same_suit[k]) == 5:
            return('Flush')

    for x in range(len(same_rank)):
        if same_rank.count(same_rank[x]) == 3:
            return('Three of a kind')

    for a in range(len(same_rank)):
        if same_rank.count(same_rank[a]) == 2:
            return('one pair')




# Test cases
four_of_a_kind = [Card(4), Card(17), Card(30), Card(5), Card(43)]
flush = [Card(40), Card(43), Card(47), Card(41), Card(50)]
three_of_a_kind = [Card(4), Card(17), Card(1), Card(5), Card(43)]
one_pair = [Card(48), Card(44), Card(35), Card(28), Card(0)]

print(poker_hand(four_of_a_kind)) # should return 'Four of a kind'
print(poker_hand(flush)) # should return 'Flush'
print(poker_hand(three_of_a_kind)) # should return 'Three of a kind'
print(poker_hand(one_pair)) # should return 'One pair'