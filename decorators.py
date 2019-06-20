# higher oder function and closure
# closure: the inner function still remembers and still have access to the variable in the scope where it was created
# even the outer function has finished executing!

def get_remainder(n):
    def three_remainder(n):
        return f"the remainder after dividing 3 is {n%3} because n is {n}"
    def five_remainder(n):
        return f"the remainder after dividing 5 is {n%5} because n is {n}"

    if n % 2 == 0: # even for this function
        return three_remainder

    else: # odd for this function
        return five_remainder

short_cut_func = get_remainder(14) # 固定好short_cut_func为three_remainder
print(short_cut_func.__name__)
print(short_cut_func(13)) #   函数不会走five_remainder
print(short_cut_func(12))


def get_remainder_without_parameter(n):
    def three_remainder():
        return f"the remainder after dividing 3 is {n%3} because n is {n}"
    def five_remainder():
        return f"the remainder after dividing 5 is {n%5} because n is {n}"

    if n % 2 == 0: # even for this function
        return three_remainder

    else: # odd for this function
        return five_remainder

short_cut_func = get_remainder_without_parameter(12) # 固定好short_cut_func为"修饰后的"three_remainder但不接受任何参数！
print("version 2:", short_cut_func.__name__)
print("version2 without parameter: ",short_cut_func()) # 依然把n记着的, closure!!
print("version2 without parameter: ", short_cut_func())

# 外部函数相当于是decorator, 利用外部传进的参数（num, msg, 甚至可以是函数）给内部函数进行"装饰"，甚至改变其内部函数的作用，
# 利用return语句吧内部函数的地址暴露出来，就可以直接call内部函数，这样就达到同一个外部函数传不同参数可以做不同事情的目的


import logging
import functools



logging.basicConfig(filename="decorator - example.log", level= logging.INFO)
def logger(func):
    @functools.wraps(func)  # 为了让the function to be passed in 的meta data 保留
    def wrapper(*args,**kwargs):

        """This is a wrapper function to wrap the function to be passed in or to be decorated"""
        logging.info(f"Running {func.__name__} with arguments {args}")
        print("calculation result:", func(*args))

    return wrapper

def add(a,b):
    """add two values together"""
    return a+b

def sub(a,b):
    """subtract two values """
    return a-b



add_logger = logger(add) # logger()的多面性
add_logger(3, 8)

sub_logger = logger(sub)
sub_logger(10,1)

# using syntactic sugar
@logger
def multiply(a,b):
    """multiply two values """
    return a * b

multiply(3,4)

@logger
def divide(a,b):
    """divide two values """
    return a/b

divide(15,5)


help(multiply)
print(multiply.__name__)
print(multiply.__doc__)


# decorator example 2:
from time import time
def speed_test(fn):
    @functools.wraps(fn)
    def wrapper(*args, **kwargs):
        print("Here is args:", args)
        print("Here are the kwargs: {}".format(kwargs))
        total_t1 = time()
        for arg in args + tuple(kwargs.values()): # 不定参数的获取方式！!!!
            t1 = time()
            result = fn(arg)
            t2 = time()
            print(f"time elapsed : {t2-t1} for the value {arg} with sum of {result}")

        total_final_t1 = time() - total_t1
        print(f"total time elapse: {total_final_t1}")
        return total_final_t1

    return wrapper


@speed_test
def sum_nums_listCompre(n):
    return sum([i for i in range(n)])

@speed_test
def sum_nums_generator(n):
    return sum(i for i in range(n))

sum_nums_listCompre(100,10000,100000, a= 9999999, b = 7777)
sum_nums_generator(100,10000,100000, a= 9999999, b = 7777)


# example 3
from functools import wraps


def ensure_authorized(fn):
    @wraps(fn)
    def wrapper(*args, **kwargs):
        if kwargs.get("role") == 'admin':
            return fn(*args, **kwargs)
        return "Unauthorized"
    return wrapper


@ensure_authorized
def show_secrets(*args, **kwargs):
    return "Shh! Don't tell anybody!"

print(show_secrets(role="admin")) # "Shh! Don't tell anybody!"
print(show_secrets(role="nobody") )# "Unauthorized"

# decorator with parametre
def ensure_first_arg_is_val(val):
    def inner(fn): #  多写一层inner
        @wraps(fn)
        def wrapper(*args, **kwargs):
            if args and args[0] != val:
                return f"first arg needs to be {val}"
            return fn(*args, **kwargs)
        return wrapper
    return inner


 # The following equals this: fav_countryX = ensure_first_arg_is_val("China") (fav_country)
 # ensure_first_arg_is_val("China")拿到inner函数地址，也就是inner(fn), 也就是拿到wrapper地址并执行wrapper(参数)，
 # 也就是执行fn(参数) 所以 fav_countryX (参数) 等价于 fn(参数)
@ensure_first_arg_is_val("China")
def fav_country(*countries):
    return countries

print(fav_country("China", "Spain", "Canada","Argentina"))
print(fav_country("Spain", "Canada","Argentina"))

# example with enforcing types

def ensure_argument_types(*types):
    def inner(fn):
        @wraps(fn)
        def wrapper(*args, **kwargs):
            my_list = [t(a) for (a,t) in zip(args,types)]
            return fn(*my_list,**kwargs)
        return wrapper
    return inner

@ensure_argument_types(str,int) # forcing inputing types
def print_string_for_multiple_times(content,times):
    for i in range(times):
        print(content)

@ensure_argument_types(float,float)
def my_divide(a,b):
    print("The divide result:", a/b)

print_string_for_multiple_times("Hahahah","3")
my_divide(1,2)

# example sleep
from time import sleep

def delay(sleep_duration):
    def inner(fn):
        @wraps(fn)
        def wrapper(*args, **kwargs):
            print("Waiting {}s before running say_hi".format(sleep_duration))
            sleep(sleep_duration)
            return fn(*args, **kwargs)

        return wrapper

    return inner

@delay(3)
def say_hi():
    return "hi"

print(say_hi())
