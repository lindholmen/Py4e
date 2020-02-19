from collections import namedtuple
# Fluent Python中使用namedtupe来做card类:
Card = namedtuple("Card",['rank',"suit"])
class ClassicDeck():
    ranks = [str(n) for n in range(2,11)] + list("JQKA")
    suits = "spades diamonds clubs hearts".split()

    def __init__(self):
        self._cards = [Card(rank,suit) for rank in self.ranks for suit in self.suits]

    def __len__(self):
        return len(self._cards)

    def __getitem__(self, pos): # to make deck iterable!!
        return self._cards[pos]




deck = ClassicDeck()
print(deck[2])
print(len(deck))
print(deck[2:6])
from random import choice
print("random:",choice(deck))

# print out last 8 cards
i = 8
for card in reversed(deck):
    if i > 0:
        print("reversed:",card)
        i = i-1
    else:
        break

# sorting
suit_values = dict(spades = 3, hearts = 2, diamonds = 1, clubs = 0)
def spade_high(card):
    rank_value = ClassicDeck.ranks.index(card.rank)
    return rank_value * len(suit_values) + suit_values[card.suit]

for card in sorted(deck, key = spade_high):
    print("sorted:",card)


print(dir(ClassicDeck))
