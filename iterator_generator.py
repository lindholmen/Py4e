# iterator > object that can be iterated upon. an object which returns data when next() is called upon it. next(iterator)
# iterable > an object will return an iterator when iter() is called upon it.e.g.  'Hello'

greeting = "Hello"
string_iterator = iter(greeting)


# print(next(string_iterator))
# print(next(string_iterator))
# print(next(string_iterator))
# print(next(string_iterator))
# print(next(string_iterator))


def my_for(iterable, func):
    it = iter(iterable)  # important but like void pointer
    while True:
        try:
            data = next(it)  # important

        except StopIteration:
            break

        else:
            func(data)


def square(x):
    print(x * x, end = " - ")


my_for(greeting, print)

my_for([1, 2, 3, 4], square)
print()

# custom iterator used in for loop
class Counter:
    def __init__(self, low, high):
        self.current = low
        self.high = high

    # for loop will always call iter(), i.e. go to call __iter__ FIRST, which SHOULD return an iterator object
    # THEN next() will be auto called on iterator object which leads to __next__ that is already implemented by default!
    # but here the returned object is self, which is not an iterator object,
    # so we need to have a manually defined __next__ call to handle next() call

    def __iter__(self):
        return self  # here return an instance of the class with current = 0 and high = 10, which is not an iterator type so we had to mannually write __next__.

    # In the __next__ call, instance's current value needs to be returned to x for printing and then it adds 1
    # until at somepoint it raise the exception
    def __next__(self):
        if self.current < self.high:
            num = self.current
            self.current = self.current + 1
            return num
        # The for loop won't print the StopIteration exception,
        # it's designed to stop the loop when the next() call raises StopIteration.
        # Therefore, the Python for loop listens for StopIteration as a sign to end the loop,
        # but it's NOT set up to show the exception to the user, because this is an expected behavior in the for loop procedure
        # a for loop will implicitly catch the StopIteration exception
        raise StopIteration # it will AUTOMATICALLY STOP
#模拟range()
for x in Counter(0, 5):
    print(x, end=' . ')


# example 2
print()
class StrRange:
    def __init__(self, text):
        self. text = text
        self.i = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.i < len(self.text):
            returned_char = self.text[self.i]
            self.i = self.i + 1
            return returned_char
        raise StopIteration

for x in StrRange("Yemao"):
    print(x, end=' . ')

# example 3
class PrintNumber:
    def __init__(self, max):
        self.max = max

    def __iter__(self):
        self.num = 0
        return self

    def __next__(self):
        if(self.num >= self.max):
            raise StopIteration
        self.num += 1
        return self.num

printNum = PrintNumber(3)

printNumIter = iter(printNum)

print()
# prints '1'
print("starting from 1:", next(printNumIter))

# prints '2'
print("starting from 1:",next(printNumIter))

# prints '3'
print("starting from 1:",next(printNumIter))

# raises StopIteration and since this is not a for loop it will really raise the exception which none could catch!!!!!
#print(next(printNumIter))

# example 4 for deck of cards
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

    # the for loop will always call for iter() of the object, then goes to __iter__ method
    # do not need to define __next__  here because if the returned is an iterator type
    # then iterators already have __next__ properly defined by default.
    # but previous example of class Counter, it returned the Counter self instance (which is not an iterator type!)
    # so the next() needs to be added manually.

    def __iter__(self):
        return iter(self.cards)

    ##### or use generator########
    #   for card in self.cards:
    #       yield card
    ##### or use generator########


    # def _deal(self, number):
    #     if number < self.count():
    #         self.dealed_cards = self.cards[-number:]
    #         self.cards = self.cards[:-number]
    #         return self.dealed_cards
    #     elif self.count() > 0:
    #         self.dealed_cards = self.cards.copy()
    #         self.cards.clear()
    #         return self.dealed_cards
    #     else:
    #         raise ValueError("All cards have been dealt")

    def shuffle(self):
        if self.count() == 52:
            random.shuffle(self.cards)
            return self
        else:
            raise ValueError("Only full decks can be shuffled")

    # def deal_card(self):
    #     self._deal(1)
    #     return self.dealed_cards[0]
    #
    # def deal_hand(self, number):
    #     self._deal(number)
    #     return self.dealed_cards

newdeck = Deck()
print(newdeck)

newdeck.shuffle()

for card in newdeck:
    print(card)

# generator function

def count_up_to_max(max):
    count = 1 # starts at 1
    while count <= max:
        yield count # will return the value of counter and pause,resume until next()is called on that yielded generator
        # same generator object just got updated!!!
        count += 1

mygen = count_up_to_max(5)
print(next(mygen)) # everytime
print(next(mygen))
print(next(mygen))
print(next(mygen))
print("*****************")
print(next(count_up_to_max(4))) # everytime we create a brand new generator
print(next(count_up_to_max(4)))
print(next(count_up_to_max(4)))
print(next(count_up_to_max(4)))

mygen = count_up_to_max(10)
for num in mygen:
    print(num)

# generator function 2:

def week():
    weekday_list = ["Monday",'Tuesday','Wednesday','Thursday','Friday','Saturday','Sunday']
    for every_day in weekday_list:
        yield every_day

days = week()
print(next(days))
print(next(days))
print(next(days))
print(next(days))
print(next(days))
print(next(days))
print(next(days))

# generator function 3:

def yes_or_no():
    n = 0
    listofYN = ["yes","no"]
    while True:
        yield listofYN[n % 2]
        n = n+1
        # yield answer
        # answer = "no" if answer == "yes" else "yes"

gen = yes_or_no()
print(next(gen)) # 'yes'
print(next(gen)) # 'no'
print(next(gen)) # 'yes'
print(next(gen)) # 'no'

# generator function4:
print("beer song:")
def make_song(bottle = 99, bev = "soda"):
    # while bottle >= 0:
    #     if bottle > 1:
    #         yield "{} bottles of {} on the wall.".format(bottle, bev)
    #     elif bottle == 1:
    #         yield "Only 1 bottle of {} left!".format(bev)
    #     else:
    #         yield 'No more {}!'.format(bev)
    #     bottle = bottle - 1
    for num in range(bottle, -1, -1): # range用法
        if num > 1:
            yield "{} bottles of {} on the wall.".format(num, bev)
        elif num == 1:
            yield "Only 1 bottle of {} left!".format(bev)
        else:
            yield "No more {}!".format(bev)

default_song = make_song()
for i in range(10):
    print(next(default_song))

# generator function5 vs normal function：
print("fibbonacci for generator:")
def fib(max):
    nums = []
    a, b = 0,1
    while len(nums) < max:
        nums.append(b)
        a, b = b, a + b
    return nums

print(fib(10))

def fib_gen(max):
    x, y, count = 0, 1, 0
    while count < max:
        yield y
        x, y, count = y, x+y, count+1

for n in fib_gen(10):
    print(n)

# generator function 5:
print("get multiples:")
def get_multiples(st = 1, max = 10):
    ct = 0
    step = st
    while ct < max:
        yield st
        st = st + step
        ct += 1

for n in get_multiples(2,3):
    print(n)

print("get unlimited multiples")
def get_unlimited_multiples(st = 1):
    step = st
    while True:
        yield st
        st = st + step
it = get_unlimited_multiples(7)
print([next(it) for i in range(10)])

# genenerator expression
print("generator expression time:")
import time
gen_start_time = time.time()
print(sum(n for n in range(10000000)))
gen_stop = time.time() - gen_start_time


lst_start_time = time.time()
print(sum([n for n in range(10000000)]))
lst_stop = time.time() - lst_start_time

print(f"took {gen_stop} for generator to calculate sum.")
print(f"took {lst_stop} for list comprehension to calculate sum.")

# class for generator funciton:

class GongAttackPool:
    attack_suspend = False

    def generate_attack(self):
        while not self.attack_suspend:
            yield "摩擦大毛"



att_pool = GongAttackPool()
gong_generator = att_pool.generate_attack()
print("Attack 5 rounds:", [next(gong_generator) for attack in range(5)])
# Attack 5 rounds: ['摩擦大毛', '摩擦大毛', '摩擦大毛', '摩擦大毛', '摩擦大毛']

# for x in gong_generator: ## generator 经典用法之一 : generator is iterable !!!
# #     print(x) ## infinite loop 输出

#att_pool.attack_suspend = True
#print(next(gong_generator)) # stop iteration
#att_pool.attack_suspend = False
#print(next(gong_generator)) # stop as well, new to create new generator to make it work


