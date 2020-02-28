#! /usr/bin/env python3
import copy

# mylist = [[0,0,0] for i in range(4)]
# print(id(mylist[0]),id(mylist[1]),id(mylist[2]),id(mylist[3]))
# mylist[0][1] = 9 # will get [[0, 9, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0]]
# print(mylist)
#
# mylist2 = [[0,0,0]]*4
# print(id(mylist2[0]),id(mylist2[1]),id(mylist2[2]),id(mylist2[3]))
# mylist2[0][1] = 9
# print(mylist2) # will get [[0, 9, 0], [0, 9, 0], [0, 9, 0], [0, 9, 0]]

# shallow copy

xs = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
ys = list(xs) #shallow copy by factory function, copy in the level 1
ys.append(["something new"])
print(f"change at the superficial level is fine. ys: {ys} and xs:{xs}")
xs[1][0] = "X"
print(f"children are not copied but only referenced> ys: {ys} and xs:{xs}")


# deep copy
xs = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
zs = copy.deepcopy(xs) # contrast> copy.copy() for shallow copy
xs[1][0] = 'X'
print(f"children are copied > zs: {zs} and xs:{xs}")


# shallow copy for class

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def __repr__(self):
        return f'Point({self.x!r}, {self.y!r})'

class Rectangle:
    """doc string for rectange"""
    def __init__(self, topleft, bottomright):
        self.topleft = topleft
        self.bottomright = bottomright
    def __repr__(self):
        return (f'Rectangle({self.topleft!r}, '
                f'{self.bottomright!r})')

rect = Rectangle(Point(0, 1), Point(5, 6))
srect = copy.copy(rect)
rect.topleft.x = 999
print("rect:",rect)
print("srect:",srect)

# deep copy for class
drect = copy.deepcopy(srect)
drect.topleft.x = 222
print("drect:", drect)
print("srec:", srect)
