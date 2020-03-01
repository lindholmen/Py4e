from collections import namedtuple

# nametuple: Factory Function for Tuples with Named Fields
Person = namedtuple("Person", ["name","age", "sex"])
p1 = Person("Jason", 30, sex = "Man")
p2 = Person("Merry", 60, sex = "Woman")
print("person's information:", p1.name, p1.age, p1.sex)
print(p2)

# 三个自带方法
# unpacking like a regular tuple
name, age, sex = p1
print("unpacking:", name, age, sex)

# New an OrderedDict
mydict = p1._asdict()
print("OrderDict:", mydict.get("name"), mydict.get("age"), mydict.get("sex"))

# Return a new instance of the named tuple
new_person = p1._replace(name = "Kitty", age = 1, sex = "Woman")
print(new_person)

# make new instances with existing iterables
p3 = Person._make(["Kobe",38, "Man"])
print("_make an instance:",p3)

# 几种常用用法
# 1. 把dict转为namedtuple
mydict2 = {"name": "X", "age": 30, "sex": "Woman"}
print("\nDict to namedtuple:", Person(**mydict2))


# 获取csv或者sqlite3的数据文件中的record,使用_make以及map方法
print("\nRead csv file 'users.csv':")
import csv
Name = namedtuple("Name", ["first","last"])
for nm in map(Name._make, csv.reader(open("users.csv"))):
    print(nm.first,nm.last)

print("\nConnect sqlite3  file 'my_friends.db':")
import sqlite3
conn = sqlite3.connect('my_friends.db')
cursor = conn.cursor()
cursor.execute('select * from friends where closeness > 700 order by closeness')
Friend = namedtuple("Friend", ["first",'last','closeness'])
for frd in map(Friend._make, cursor.fetchall()):
    print(frd.first,frd.last,frd.closeness)


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
        print(card)
        i = i-1
    else:
        break

# sorting
suit_values = dict(spades = 3, hearts = 2, diamonds = 1, clubs = 0)
def spade_high(card):
    rank_value = ClassicDeck.ranks.index(card.rank)
    return rank_value * len(suit_values) + suit_values[card.suit]

for card in sorted(deck, key = spade_high):
    print(card)


