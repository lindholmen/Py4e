#! /usr/bin/env python3

##  ways of creating the same dict

dict_1 = dict(name = "kkk", age = 36)
dict_2 = {"name": "kkk", "age":36}
dict_3 = dict({'a':1,'b':2},c=3,d=4)
dict_4 = dict([('a',1),('b',2)],c=3)
print(dict_3)
print(dict_4)

person_information = { "name" : "YM", "age" : 31, "job" : "researcher", "sex" : "M", "livingInSweden" : True}
person_information.setdefault("citizenship", "China") # if not exist then add it
person_information2= {}.fromkeys(['name',"sex"],"unknown") # create key value pairs - set multiple defaults 必须第一传入list


for key,value in person_information2.items():
    print(f"Key information '{key}': Value info '{value}'")

for key in person_information:
    print("key：",key)
    print("value:",person_information[key])


print("Religion is " , person_information.get("Religion")) # 不存在的key,返回第二个参数否则为None

#converting keys() as a set to list
print(list(person_information.keys()))

# DON'T TOUCH PLEASE!
donations = dict(sam=25.0, lena=88.99, chuck=13.0, linus=99.5, stan=150.0, lisa=50.25, harrison=10.0)
# DON'T TOUCH PLEASE!

# Use a loop to add together all the donations and store the resulting number in a variable called total_donations
total_donations = sum(donations.values())
total_donations2 = sum(donation for donation in donations.values()) #Lambdas and Built-In Functions, same as above
print(total_donations,total_donations2)

#person_information.clear()
#print(person_information)

copy_person_information = person_information.copy()
print(copy_person_information)
if (copy_person_information is not person_information):
    print("copy objects do not share the same memory!")

# Delete
del copy_person_information['age']
print("copy_person_information after del:", copy_person_information)
copy_person_information.pop("name")
print("copy_person_information after pop:",copy_person_information)
copy_person_information.popitem()
print("copy_person_information after popitem:",copy_person_information)

copy_person_information.update(dict_1)
print("copy_person_information after update:",copy_person_information)

#dictiionary comprehension  {__：__ for xx in xx}
numbers = dict(first = 1, second = 2, third = 3)
squarenumbers = { key: value ** 2 for key,value in numbers.items() }
print("dict comprehension:", squarenumbers)
print("squre dict:", {key: key**2 for key in range(1,6)})
stringA = "ABC"
stringB = "123"
print("string pair dict:", { stringA[i]:stringB[i] for i in range(0,len(stringA))})

list1 = ["CA", "NJ", "RI"]
list2 = ["California", "New Jersey", "Rhode Island"]
print("zip dict用法:",dict(zip(list1,list2))) # zip is to return tuple
print("zip list 用法:",list(zip(list1,list2)))


numbers = [1,2,3,4,5,6,7]
numbers_odd_even = { key: "even" if key%2 == 0 else "odd" for key in numbers }
print(numbers_odd_even)

# unpack, 只要给的参数个数是内嵌结构的个数！
listofPairs = [["name", "jack"],["age",31]]
unpackDict = { k:v for k,v in listofPairs}
print("unpacking nested 2 elements:", unpackDict)

listofPairs = [(1,2,3),(4,5,6)]
unpackList = [ a+b+c for a,b,c in listofPairs ]
print("unpacking nested 3 elements:", unpackList)


# sorted
D = {"a":1,"c":2, "b":3}
for key in sorted(D):
    print(f"{key} --> {D[key]}")

# tuple and set, faster than list and immutable
mytuple = (1,2,3)
tupletoadd = (4,5)
mytuple = mytuple + tupletoadd
print("tuple concatenation --> " ,mytuple)

locations = {(35, 39): "Shanghai",
(76,77):"sweden"
}

print(" locations -->",locations)

names = ("Jack","Nick","Steve")
for name in names:
    print(f"iterate in a tuple> {name}")

print("nick's index :", names.index("Nick"))
print("reversed tuple", names[::-1])

#set, no order or duplicate
myset = {2,4,6,8,10}
myset2= set({1,2,3,4,5})
myset.add(100)
print("adding element in a set:",myset)
myset.remove(100)
myset.discard(2)
print("removing element in a set:",myset)
print(myset|myset2) # union
print(myset&myset2) # 4, intersection


#set comprehension
string = "hello world"
print("set comprehension:", {char for char in string if char in 'aeiou'})

# grumpy dic
print()
print("*******************dictionary magic method*******************")
class GrumpyDict(dict):
    def __repr__(self):
        print("NONE OF YOUR BUSINESS")
        return super().__repr__()

    def __missing__(self, key):
        print(f"YOU WANT {key}?  WELL IT AINT HERE!")

    def __setitem__(self, key, value):
        print("YOU WANT TO CHANGE THE DICTIONARY?")
        print("OK FINE...")
        super().__setitem__(key, value)

    def __contains__(self, item):
        print("let me look!")
        return super().__contains__(item)


d = GrumpyDict({"name": "Man", "city": "chongqing"})
print(d)
d["city"] = "Gothenburg"
print(d)
print('name' in d)
grumpy_dic = GrumpyDict("")

def difference(d1,d2):
    return {k:v for k,v in d1.items() if k not in d2}

print("difference：",difference({'a':1,'b':2,'c':3},{'b':2}))


def max_key(d):
    return [] if len(d) == 0 else (max(d.keys()), d[max(d.keys())])

print("max_key:", max_key({'a':3,'c':3,'b':2}) )

def max_value(d):
    return [] if len(d) == 0 else [(k,v) for k,v in d.items() if v == max(d.values())]

print("max_value:", max_value({'a':3,'c':3,'b':2}) )

def max_overlap(dict1,dict2):
    overlap = set(dict1).intersection(dict2)
    max_value = 0
    max_i = None
    for i in overlap:
        if dict1.count(i) + dict2.count(i) > max_value:
            max_value = dict1.count(i) + dict2.count(i)
            max_i = i
    return (max_i,max_value)

print(max_overlap([1,2,2,2,3,3],[2,2,3,2,2,3]))


import heapq
portfolio = [
    {'name': 'IBM', 'shares': 100, 'price': 91.1},
    {'name': 'AAPL', 'shares': 50, 'price': 543.22},
    {'name': 'FB', 'shares': 200, 'price': 21.09},
    {'name': 'HPQ', 'shares': 35, 'price': 31.75},
    {'name': 'YHOO', 'shares': 45, 'price': 16.35},
    {'name': 'ACME', 'shares': 75, 'price': 115.65}
]

cheapest = heapq.nsmallest(3, portfolio,key= lambda x: x["price"])
print("cheapest:",cheapest)
expensive = heapq.nlargest(3, portfolio,key= lambda x: x["price"])
print("expensive:",expensive)

from collections import OrderedDict

d = OrderedDict()
d["B"] = 2
d["A"] = 1
d["C"] = 3
d["C"] = 0
for key in d:
    print(f"key:{key}, value:{d[key]}")


from collections import defaultdict
lst = [(1,'apple'),(2,'orange'),(1,'compute')]
d = defaultdict(list)
for k,v in lst:
    d[k].append(v)

print(d)


def merge_dict(dict1,dict2):
    return {**dict1, **dict2}

dic1 = {'x': 1, 'y': 2 }
dic2 = {'y': 3, 'z': 4 }
print(merge_dict(dic1, dic2))
