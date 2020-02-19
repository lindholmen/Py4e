#! /usr/bin/env python3
import sys
import math

add = lambda a,b: a+b # evaluated and returned for anonymous function


print(add(1,2))
print(add.__name__)

#In Python, we generally use it as an argument to a higher-order function
#(a function that takes in other functions as arguments).

def calculate_cube(f,x):
    return f(x)

print(calculate_cube(lambda i: i * i * i, 3))


#Lambda functions are used along with built-in functions like filter(), map() etc.



mylist = [2,3,4,5,6]
newlist1 = list(filter(lambda x: x%2 == 0, mylist))
print("lambda using in a filter():", newlist1)
newlist2 = list(map(lambda x: x*2, mylist))
print("lambda using in a map():", newlist2)

#sort dictionary:
xs = {'a': 4, 'b': 3, 'd': 1, 'c': 2}
print("items:", xs.items())
print("sort by key using dict.items() :", sorted(xs.items())) # [('a', 4), ('b', 3), ('c', 2), ('d', 1)]
print("sort by value using lambda as key:", sorted(xs.items(), key = lambda item: item[1], reverse = False)) # [('d', 1), ('c', 2), ('b', 3), ('a', 4)]
#making a new dict by value
foo = lambda value,key: "{} - {}".format(value,key)
for value, key in sorted({value:key for key, value in xs.items()}.items()):
     # {4: 'a', 3: 'b', 1: 'd', 2: 'c'}
     #print("{} - {}".format(key,value))
     print(foo(value,key))

tweets = [{"username":"nick","content": ["hello","yes"]}, {"username":"jack","content": [], "color" : "blue"}, {"username":"mamba","content": []}]
# select inactive users and print their uppercase of the user name, filter inside map:
inactive_users = list(map( lambda user:user["username"].upper() , filter(lambda u: not u["content"], tweets)))
print(inactive_users) # ["JACK","MAMBA"]
# using list comprehension
inactive_users2 = [ x["username"].upper()  for x in tweets if not x["content"]]
print(inactive_users2) # ["JACK","MAMBA"]
# using sorted
print("using sort by username:",sorted(tweets, key = lambda user: user["username"]))
print("using sort by tweet lenght:", sorted(tweets, key = lambda user: len(user['content']), reverse = True) )




# all and any
#all - if the iterable is empty or all of them are true then True
#any - if the iterable is empty or none of them is true then False

print(all([0,1,2])) # false because 0 is False

name_list = ["cathy", "cake", "cecila","jack"]
checklist = [name[0] == "c" for name in name_list]
checklist2 = [name[0] == "j" for name in name_list]
print(" All names starts with 'c'? ", all(checklist)) # false
print(" Any of them starts with 'j'?", any(checklist2))

# find the longest name, first create the list with dictionaries of names length and name content
name_dict = [{"namelength":len(name_list[index]), "namecontent":name_list[index]} for index in range(len(name_list))]
print("name dict:", name_dict)
print("using sort to find the longestname:", sorted(name_dict, key = lambda x:x['namelength'],reverse = True)[0]['namecontent'])
# or use max
print("using max and key to find the longest name:",max(name_list, key = lambda n: len(n)))

#find the song that is least played
songs = [{"title":"happy", "playcount":1},
        {"title":"sad", "playcount":10},
        {"title":"gogogo", "playcount":50},
        {"title":"dadada", "playcount":100}]
songitem = min(songs, key = lambda n: n["playcount"])
print("The least play song is :", songitem["title"])

# reversed:
reversedObj = reversed("Hello")
reversed_list = str(reversedObj)
print(reversed_list)
#print("".join(reversed_list))


#generator expression is to use the () to save the space because you use the iterating once and dont need to save it to an actual list!
# generator expression is a light weighted list but not support any list methods!!!! like index or slicing
print(" All names starts with 'c' ? (generator expression)", all(name[0] == "c" for name in name_list)) # false
list_comprehension  = sys.getsizeof([x * 10 for x in range(1000)])
list_generator  = sys.getsizeof(x * 10 for x in range(1000))
print(f"It takes {list_comprehension} bytes for list comprehension")
print(f"It takes {list_generator} bytes for list generator expression")

# math
print("\n***********Math****************")
print("using abs:", abs(float(4)))
print(f"using fabs:{math.fabs(4)}")
print("sum:", sum([1,2,3], 10))
print("sum of a set:", sum({1,2.5,3.5}))
print("round: ", round(-3.1415426, 4))
print("round:", round(3.145,2))
print("round:", round(0.5))
print("round:", round(-0.51))
print("round:", round(1.5))
print("round:", round(2.675,2)) # it’s a result of the fact that most decimal fractions can’t be represented exactly as a float.
#http://www.runoob.com/w3cnote/python-round-func-note.html
#对浮点数精度要求如果很高的话，请用decimal模块。

# zip - list of tuples
first_zip = zip([1,2,3],["a","b","c","d"])
print(list(first_zip))
print("empty dict because the iterators are exhausted after iterating over them once:\n",dict(first_zip))
print(dict(zip(["a","b","c","d"], [1,2,3])))
print(list(zip(["haha", "yes","no"], [1,2,3], ["M","y","z"])))

mylistforunpacking = [(0,1),(2,3),(4,5)]
print("first unpacking then zip:",list(zip(*mylistforunpacking)))

mid = [80,91,78]
final = [98,89,53]
students = ['kate',"james","russel"]

scorelist = [max(i) for i in list(zip(mid, final))]
student_score_dict = dict(zip(students,scorelist))
print(student_score_dict)

three_zip = zip(students, mid, final)
final_grade = {triplet[0]: max(triplet[1],triplet[2]) for triplet in three_zip}
print(final_grade)

lambdascorelist = list(map(lambda x: max(x), zip(mid, final)))
print(dict(zip(students, lambdascorelist)))

def interleave(str1, str2):
    new_zip_str_list = list(zip(str1,str2))
    new_zip_str_list_woven = ["".join(i) for i in new_zip_str_list]
    return "".join(new_zip_str_list_woven)

print(interleave("lzr","iad")) # output lizard

def triple_and_filter(l):
    return list(map(lambda y: y*3, list(filter(lambda x: x%4 == 0, l))))

print(triple_and_filter([6,8,10,12])) # [24,36]


def extract_full_name(l):
    return list(map(lambda x : "{} {}".format(x["first"],x["last"]), l))

names = [{'first': 'Elie', 'last': 'Schoppik'}, {'first': 'Colt', 'last': 'Steele'}]
print(extract_full_name(names)) # ['Elie Schoppik', 'Colt Steele']