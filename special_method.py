from math import hypot

class Vector:
    def __init__(self, x = 0, y = 0):
        self.x = x
        self.y = y

    def __repr__(self):
        #return f"Vector({self.x},{self.y}) at {id(self)}"
        return f"Vector({self.x},{self.y})"

    # choose repr over str as str is used to provide readable info
    # def __str__(self):
    #     return f"This is a vector({self.x},{self.y})"

    def __abs__(self):
        return hypot(self.x, self.y)

    def __add__(self, other):
        x = self.x + other.x
        y = self.y + other.y
        return Vector(x,y)

    def __mul__(self, scalar):
        return Vector(self.x*scalar,self.y*scalar)



v1 = Vector(3,4)
v2 = Vector(4,5)

print(v1)
print(v2)
print(abs(v1))
v3 = v1+v2
print(v3)
print(v1 * 3)

import ctypes

def ref_count(address):
    return ctypes.c_long.from_address(address).value

print(ref_count(id(v3)))
print(bool(v3))
print(dir(Vector))

import argparse


def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('-c',
                        '--config',
                        default='ds_config')  # # Assign config file, don't use '.py' suffix.
    parser.add_argument('-s',
                        '--spider',
                        help='',
                        default='spider_sample')  # Assign spider file, don't use '.py' suffix.
    parser.add_argument('-t',
                        '--thread_count',
                        help='',
                        default=0,
                        type=int)
    return parser.parse_args()


if __name__ == '__main__':
    args = parse_args()
    print(args.config)
    print(args.spider)
    print(args.thread_count)