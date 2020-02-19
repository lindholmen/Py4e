import random as omg_so_random
from random import randint

import keyword
#import banana
from banana import peel

hero_list = ["Tiny","Slark","Axe", "Clock", "Bara", "PA"]
print(omg_so_random.choice(hero_list))
omg_so_random.shuffle(hero_list)
print(hero_list)
print(randint(1,100))

def contains_keyword(*args):
    return any(keyword.iskeyword(item) for item in args)

print(contains_keyword("def","haha","yes","no"))

def ready_to_peel():
    print(f"Hi! My __name__ is {__name__}") # if the file is the main file being run its value is "__main__"

ready_to_peel()
print(peel()) # otherwise it is going to be the file name!!



