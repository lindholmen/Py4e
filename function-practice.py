from random import random

#
# mylist = [[0,0,0] for i in range(4)]
# print(id(mylist[0]),id(mylist[1]),id(mylist[2]),id(mylist[3]))
# mylist[0][1] = 9 # will get [[0, 9, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0]]
# print(mylist)
#
# mylist2 = [[0,0,0]]*4
# print(id(mylist2[0]),id(mylist2[1]),id(mylist2[2]),id(mylist2[3]))
# mylist2[0][1] = 9
# print(mylist2) # will get [[0, 9, 0], [0, 9, 0], [0, 9, 0], [0, 9, 0]]

r = 0

def flip_copy():
    r = random() # 如果没有global则是local variable
    if r>0.5:
        print("Heads")
    else:
        print("Tails")



def defaultEx(m,n = 2, note=flip_copy ): #  parameter could be a function but it gotta be the last parameter
    """ exponent(a,b) returns a ** b, b default to 2  """
    note()
    return m**n

print(defaultEx(8))
print(defaultEx.__doc__)


def print_name(first, last):
    return f"{first} {last}"

print(print_name(last = "man",first = "nick")) # keyword argument, order does not matter anymore


mylist = [1,2,3]
def test_pop(lst):  ## 没有实参形参的说法，都是实际参数！！！
    return(lst.pop())
print("pop elem:", test_pop(mylist))
print("my list now is :", mylist)


#使用 list comprehension 没有elif就用else "xxx" if...
def number_compare(a,b):
    mylist = ["First is greater" if a > b else "Second is greater" if b>a else "Two are equal" for i in range(1)]
    # or even this : def number_compare(a,b):
    # return "First is greater" if a > b else "Second is greater" if b > a else "Numbers are equal"
    print(mylist[0])

number_compare(1,0)

def is_palindrome(input_string):
    processed_string = input_string.lower().replace(" ","") # 去除string中所有的whitespace
    back_string = processed_string[::-1]
    return back_string == processed_string

print(is_palindrome("amanaplanacanal Panama"))


listA = [1,2,3]
listB = [3,4,5]
setA = set(listA)
setB = set(listB)
print("intersection:", [ v for v in (setA & setB)])
print("intersection2:",[ x for x in listA if x in listB])


#*args/**kwargs has its advantages, generally in cases where you want to be able to pass in an unpacked data structure, while retaining the ability to work with packed ones
def sum_num(*args): # *args 表示任意个数的参数 ，且args是一个tuple （被packed起来了, 收敛）
    print("printing args ->", args)
    count = 0
    for i in args:
        count += i
    return count

print(sum_num(1,2,3))
print(sum_num(2,3,4,5)) #直接传入unpack的参数，即没有封装成list,dict or tuple的散装参数，个数不定

# *还可以unpack argument list or tuple, 传入一个多参数的函数， （发散）
mylist = [1,2,3]
print("unpacking>", *mylist) # 1 2 3
def foo(a,b,c):
    print("unpacking to make the call to print out>",a,b,c)

def foo2(*args):
    total = 0
    for i in args:
        total += i
    print("foo2, the sum of unpacking is :", total)
foo(*mylist)
foo2(*mylist)

# In Python 3 it is possible to use *l on the left side of an assignment
first, *l, last = [1,2,3,4,5]
print("l in the middle is a list:", l)

# The **kwargs will give you all keyword arguments as dictiionary
#The double ** means there can be any number of extra named parameters.

def bar(param1, **kwargs):
    print(param1)
    print("** means a dictionary of keyword arguments ->",kwargs)
    for x in kwargs:
        print(x,kwargs[x])

bar(1, name = "nick", age = 28, sex = "M")

def display_info(a, b, *args, role = "researcher", **kwargs): # order matters!!
    print( [a,b, args, role, kwargs] )

display_info("Nick","Man","China", age = 28, hobby = "Dota")

# **还可以unpack dictionary to keyword argument
def display_name(first, second, **kwargs):
    print(f"Hello, {first} {second}!")
    print("something else in the keyword arguments:")
    print(kwargs)

name_info_dict = {"first":"Jack", "second":"Ma", "job":"CEO", "age" : 50, "Married" : False}
display_name(**name_info_dict, SomethingElse= "None yet") # unpack it to keyword argument then use key word argument to pass into the function
#注意something else也被包涵进入kwargs


## Python 3.5+ supports 'type annotations' that can be
# used with tools like Mypy to write statically typed Python
def my_add(a: int, b: int) -> int:
    return a + b
print(my_add(1,2))



def multiply(*args):
    total = 1
    for arg in args:
        total = total * arg
    return total

def apply(*args, operator):
    if operator == "*":
        return multiply(*args) # 这里必须unpack, 否则传入（2,3,4） 到multiply, args== （（2，3，4），）
    elif operator == "+":
        return sum(args)
    else:
        return "no valid operator"

apply_result = apply(2,3,4,operator = "*")
print(f"apply : {apply_result}")
