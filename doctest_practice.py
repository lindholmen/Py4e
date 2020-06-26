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