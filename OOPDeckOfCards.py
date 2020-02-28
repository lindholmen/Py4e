import random

# class Card:
#     def __init__(self, suit, value):
#         self.suit = suit
#         self.value = value
#
#     def __repr__(self):
#         return f"{self.value} of {self.suit}"
#
#
# class Deck:
#     suit_list = ["Hearts","Diamonds","Clubs","Spades"]
#     value_list = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]
#     def __init__(self):
#         self.list_of_cards = [ Card(s,v) for s in Deck.suit_list for v in Deck.value_list]
#         self.dealed_cards = []
#
#     def count(self):
#         return len(self.list_of_cards)
#
#     def __repr__(self):
#         return f"Deck of {self.count()} cards"
#
#     def _deal(self,number):
#         if number < self.count():
#             self.dealed_cards = self.list_of_cards[:number]
#             self.list_of_cards = self.list_of_cards[number:]
#         elif self.count() > 0:
#             self.dealed_cards = self.list_of_cards.copy()
#             self.list_of_cards.clear()
#         else:
#             raise ValueError("All cards have been dealt")
#
#     def shuffle(self):
#         if self.count() == 52:
#             random.shuffle(self.list_of_cards)
#             return self
#         else:
#             raise ValueError("Only full decks can be shuffled")
#
#     def deal_card(self):
#         self._deal(1)
#         return self.dealed_cards[0]
#
#     def deal_hand(self,number):
#         self._deal(number)
#         return self.dealed_cards

import random


class Card:
    def __init__(self, suit, value):
        self.suit = suit
        self.value = value

    def __repr__(self):
        return self.value + " of " + self.suit


class Deck:
    suit_list = ["Hearts", "Diamonds", "Clubs", "Spades"]
    value_list = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]

    def __init__(self):
        self.cards = [Card(s, v) for s in Deck.suit_list for v in Deck.value_list]
        self.dealed_cards = []

    def count(self):
        return len(self.cards)

    def __repr__(self):
        return "Deck of " + str(self.count()) + " cards"

    def _deal(self, number):
        if number < self.count():
            self.dealed_cards = self.cards[-number:]
            self.cards = self.cards[:-number]
            return self.dealed_cards
        elif self.count() > 0:
            self.dealed_cards = self.cards.copy()
            self.cards.clear()
            return self.dealed_cards
        else:
            raise ValueError("All cards have been dealt")

    def shuffle(self):
        if self.count() == 52:
            random.shuffle(self.cards)
            return self
        else:
            raise ValueError("Only full decks can be shuffled")

    def deal_card(self):
        self._deal(1)
        return self.dealed_cards[0]

    def deal_hand(self, number):
        self._deal(number)
        return self.dealed_cards

newdeck = Deck()
print(newdeck)

newdeck.shuffle()

card = newdeck.deal_card()
print(card) # 6 of Diamonds

hand = newdeck.deal_hand(20)
print(hand) # [8 of Spades, 5 of Hearts, 4 of Diamonds, 5 of Clubs, 10 of Clubs, Q of Clubs, 3 of Diamonds, 2 of Spades, 9 of Hearts, 7 of Clubs, 10 of Spades, 9 of Clubs, 10 of Hearts, A of Clubs, Q of Hearts, 8 of Diamonds, 2 of Clubs, K of Hearts, 7 of Diamonds, 2 of Diamonds]

hand = newdeck.deal_hand(10)
print(hand) # [A of Spades, 4 of Hearts, 9 of Spades, K of Spades, 6 of Spades, 2 of Hearts, K of Diamonds, A of Diamonds, 3 of Spades, J of Clubs]

