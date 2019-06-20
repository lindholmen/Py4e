#! /usr/bin/env python3

# print("something to add in the shopping cart")
#
# input_char = input("add something to the cart?")
# shopping_list = []
# while input_char != 'q':
#     shopping_list.append(input_char)
#     input_char = input("add something to the cart?")
#
# shopping_list.sort()
# # for i in range(len(shopping_list)):
# #     print(f"--{shopping_list[i]}--")
#
# for i in shopping_list:
#     print(f"--{i}--")

mylist = [[] for i in range(4)]  # deep copy
mylist[1] = "true".upper()
mylist[3] = 4
print(mylist)

myshawllowcopylist = [[0,0]]*4 # shallow copy
print("before change:",myshawllowcopylist)
myshawllowcopylist[0][0] = "something"
print("after change:",myshawllowcopylist)


my_second_list = list(range(1,4))
print(my_second_list)
if 3 in my_second_list:
    print("3 is inside the my_second_list")

index = 0
while index < len(my_second_list):
    print(f"index {index} : {my_second_list[index]}")
    index += 1

data = [1,2,3]
data.append("Hello")
print("data:",data)
dataToExtend = [4,5,6]
data.extend(dataToExtend)
print("data:",data)
data.insert(3,"World")
print("data:",data)
data.insert(-1, "second to the last") # -1 means this is the last elments position before insertion
print("data:",data)
data.pop(2)
data.pop()

data.remove("Hello") # only remove the first "hello" element, when knowing what to remove
print("data:",data)

names = ["huan","niubigong","fanfan","huan","niubigong","fanfan", "fanfan"]
print("index of niubigong  is:",names.index("niubigong"))
print("find index of fanfan starting at index 3:", names.index("fanfan", 3))
print("the count occurence of element fanfan is ", names.count("fanfan"))
names.reverse()
print("the reversed list is :",names)

print("\U0001f600".join(names))

mylist=[1,2,3,4,5,6]
newlist = mylist[:1:-1] #[6,5,4,3] 1表示结束的位置是2 but exclusive!
print("backward slicing:",newlist)

mystring = "this is a funny world!"
myreversedstring = mystring[::-1]
print("reversed string is :",myreversedstring)
print("reversed of the reversed string is :",myreversedstring[::-1])

#modifying list
numbers = [1,2,3,4,5]
numbers[1:3] = ["a","b","c"] # 插入的list的元素可以超过这个被替代的list的index范围！！！
print("modified slicing list:", numbers)

#swaping values
myList = ["Hello", "World"]
myList[0], myList[1] = myList[1], myList[0]
print("the swapped list is :",myList)

#list comprehension
M = [[1,2,3],
    [4,5,6],
    [7,8,9]]

generatedList = [row[1] for row in M if row[1]%2 == 0]
print("generatedList using list comprehension",generatedList)

diag = [M[i][i] for i in [0,1,2]]
print("diagonal:", diag)

doubles = [c*2 for c in 'spam']
print("double chars in a list:", doubles)

print("create map even:", {row: sum(M[row]) for row in range(3)})
answer = [x for x in [1,2,3,4] if (x in [3, 4,5,6]) and (x in [1,4,5,7,9])]
answer2 = [word[::-1].lower() for word in ['Elie','Tim','Matt']]
print("3个list交集：",answer)
print("Reversed names:", answer2)

# matrix (using if and else in list conprehension)
board = [[num for num in range(1,4)] for i in range(1,4)]
print("board:",board)
visBoard = [["x" if num%2 != 0 else "o" for num in range(1,4)] for i in range(1,4)]
print("visualisation of the board",visBoard)

visBoard2 = [['*' for i in range(3)] for j in range(3)]
print("visboard2 :", visBoard2)
