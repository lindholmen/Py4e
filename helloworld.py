#! /usr/bin/env python3

import pyperclip
import os
import sys
import math
import random

print("Hello World, Python on Mac!")
print("Working directory:",os.getcwd())
print("System platform",sys.platform)
print("163M"*8)

# myAttribute1 = 'meaning of life' # try the commandline, reload first and [modulename].myAttribute
myAttribute2 = ' is about to explore'
myAttribute = 'Cool'
my4 = "Try again"
print(my4[1:5],my4[-1])
my5 = my4[4:]+" " +my4[:-6]
print(my5)
list1 = list(my4)
list1[0] = 't'
print("print try again - ",''.join(list1))
print(list1)

B = bytearray(b'spam')
B.extend(b'eggs')
print(B,B.decode(), sep = "!")

pyperclip.copy('hahaha')
print(pyperclip.paste())



L = [1,2]
L.append(L)
print(L)

print(math.pi)
print(math.sqrt(49))
print(random.random())
print(random.choice([0,1,2,3]))


# while ... else
l = [1, 2, 3]
val = 10

idx = 3
while idx < len(l):
    if l[idx] == val:
        break
    idx += 1
else: # this will execute only when the while is exited normally *(no break or exception)
    l.append(val)

print(l)


# memory reference count
import ctypes

def ref_count(address):
    return ctypes.c_long.from_address(address).value


my_var = [1, 2, 3, 4]
print("ref_count:", ref_count(id(my_var)))
x2 = my_var
print("ref_count:", ref_count(id(my_var)))
x2 = None
print("ref_count:", ref_count(id(my_var)))