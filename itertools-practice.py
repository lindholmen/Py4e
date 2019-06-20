import itertools

# 3 infinite iterators to build generators

counter = itertools.count(10,2) # 2 as step, 1 as default (10,11,12,13,14....)
for p in counter:
    if p < 20:
        print(p)
    else:
        break

cs = itertools.cycle(["chalmers","kth","UU"])
n = 0
for c in cs:

    if n<6:
        print(c)
        n = n+1
    else:
        break

ns = itertools.repeat('A', 5)
for n in ns:
    print(n)

# takewhile(predicate, iterable)
# This iterator is opposite of dropwhile(), it prints the values till the function returns false for 1st time.
xs = itertools.takewhile(lambda x: (x< 6), [1,2,3,4,5,6,7,8,9])
for x in xs:
    print("using takingwhile:", x)

# groupby
gb = itertools.groupby(["abc","abc","cth","cth","cth","kth","KTH"], lambda c: c.upper())
for x,group in gb:
    print(x,":", list(group))

# permutations and chain:
for i in itertools.permutations(["3435","magic","!","@"]): # 所有的组合可能
    s = ""
    print(i)
    for z in itertools.chain(i):
        s = s+z
    print("possible combinations:",s)


