
# assert is a statement but the second parameter is the customisable msg.
# return none if it it evaluated as truthy
# or raise AssertionError()

def add_two_positive_number(a,b):
    """
    >>> add_two_positive_number(2,3)
    5
    >>> add_two_positive_number(100,200)
    300
    """
    assert a > 0 and b> 0, "both needs to be positive"
    return a+b

add_two_positive_number(1,3)
#add_two_positive_number(-1,4) # AssertionError

food = ["fries","candies","burger"]
eating = "fries"
assert eating in food, "no must eating junk food"

# using python -o assert-and-testing.py will ignore all the assertion code!!


def double(values):
	""" double the values in a list

	>>> double([1,2,3,4])
	[2, 4, 6, 8]

	>>> double([])
	[]

	>>> double(['a', 'b', 'c'])
	['aa', 'bb', 'cc']

	>>> double([True, None])
	Traceback (most recent call last):
		...
	TypeError: unsupported operand type(s) for *: 'int' and 'NoneType'
	"""
	return [2 * element for element in values]

#python3 -m doctest -v assert-and-testing.py

# doctest expect all str to have single str not double str
def say_hi():
	"""
	>>> say_hi()
	'hi'
	"""
	return "hi"


# Watch out for whitespace!
# (There's a trailing space on line 42)
def true_that():
	"""
	>>> true_that()
	True
	"""
	return True

# Order of keys in dicts matters in doctests
def make_dict(keys):
	"""
	>>> make_dict(['a','b'])
	{'a': True, 'b': True}
	"""
	return {key: True for key in keys}
#


# unit test

import unittest
from activity import eat,nap, ElectronicCar
class ActivityTest(unittest.TestCase):
	def test_eating_healthy(self):
		"""Test first thing"""
		self.assertEqual(eat("potato",is_healthy=True), "I am eating potato cuz it is healthy")

	def test_eating_unhealthy(self):
		"""Test SECOND thing"""
		self.assertEqual(eat("chips", is_healthy=False), "I am eating chips cuz Yolo")

	def test_eating_boolean(self):
		with self.assertRaises(ValueError): # need to raise a value error
			eat("pizza", is_healthy = "not a bealean so should raise an error!")


class CarTest(unittest.TestCase):
	def setUp(self):
		"""Test setup , run before every test func run """
		self.car = ElectronicCar("Volvo", battery=50)

	def test_charge(self):
		"""Test charge """
		self.car.charge()
		self.assertEqual(self.car.battery, 100)

	def test_drive(self):
		"""Test drive """
		self.assertEqual(self.car.drive(),
						 "running, Volvo!")
		self.assertEqual(self.car.battery,
						 49)

	def tearDown(self):
		pass

from OOPDeckOfCards import Card, Deck

class CardTest(unittest.TestCase):
	def setUp(self):
		self.card = Card("Diamonds","A")

	def test_init(self):
		self.assertEqual(self.card.suit, "Diamonds")
		self.assertEqual(self.card.value, "A")

	def test_repr(self):
		self.assertEqual(repr(self.card), "A of Diamonds")

class DeckTest(unittest.TestCase):
	def setUp(self):
		self.deck = Deck()

	def test_init(self):
		self.assertTrue(isinstance(self.deck.cards, list))
		self.assertEqual(len(self.deck.cards),52)

	def test_deal_sufficient_cards(self):
		cards = self.deck._deal(10)
		self.assertEqual(len(cards),10)
		self.assertEqual(self.deck.count(),42)

	def test_deal_insufficient_cards(self):
		cards = self.deck._deal(100)
		self.assertEqual(len(cards),52)
		self.assertEqual(self.deck.count(),0)

	def test_deal_no_cards(self):
		self.deck._deal(self.deck.count())
		with self.assertRaises(ValueError):
			self.deck._deal(1)

	def test_deal_hand(self):
		last_card = self.deck.cards[-1]
		dealed_card = self.deck.deal_card()
		self.assertEqual(last_card,dealed_card)
		self.assertEqual(self.deck.count(),51)

	def test_shuffle(self):
		new_cards = self.deck.cards.copy()
		self.deck.shuffle()
		self.assertNotEqual(new_cards, self.deck.cards)
		self.assertEqual(self.deck.count(), 52)

	def test_shuffle_when_not_full_cards(self):
		self.deck.deal_card()
		with self.assertRaises(ValueError):
			self.deck.shuffle()
			
if __name__ == "__main__":
	unittest.main()


