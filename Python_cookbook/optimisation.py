import timeit
import string
import time

# pre-calculation for constants
def my_func():
    a = 24 * 60
    b = (1, 2) * 5
    c = 'abc' * 3
    d = 'ab' * 11
    e = 'the quick brown fox' * 10
    f = [1, 2] * 5

print(my_func.__code__.co_consts)

# membership test will first tranfer mutable to immutable,
# list要转为tuple, set转为frozenset
# set最快
x= 0
e= 5
t1 = timeit.default_timer()
while x <1000000:
    if e in [1,2,3,4,5,6,7,8,9,10]:
        x= x+1
t2 = timeit.default_timer()
print(t2-t1)

x=0
t1 = timeit.default_timer()
while x <1000000:
    if e in (1,2,3,4,5,6,7,8,9,10):
        x= x+1
t2 = timeit.default_timer()
print(t2-t1)

x=0
t1 = timeit.default_timer()
while x <1000000:
    if e in {1,2,3,4,5,6,7,8,9,10}:
        x= x+1
t2 = timeit.default_timer()
print(t2-t1)


char_list = list(string.ascii_letters)
print(char_list)
char_tuple = tuple(string.ascii_letters)
print(char_tuple)
char_set = set(string.ascii_letters)
print(char_set)

def membershiptest(n, container):
    for i in range(n):
        if "x" in container:
            pass

test_start = time.perf_counter()
membershiptest(1000000,char_list)
test_end = time.perf_counter()
print(test_end-test_start)

test_start = time.perf_counter()
membershiptest(1000000,char_tuple)
test_end = time.perf_counter()
print(test_end-test_start)

test_start = time.perf_counter()
membershiptest(1000000,char_set)
test_end = time.perf_counter()
print("fastest is set:",test_end-test_start)

