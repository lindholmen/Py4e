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

# List and tuples
# Case 1: find if there is any repeated elements in a list
def is_duplicated(lst):
    return len(lst) != len(set(lst))

print("# Case 1: find if there is any repeated elements in a list")
print(is_duplicated([0,1,2,3,4]))
print(is_duplicated([0,1,2,4,4]))

# Case 2: find all duplicated elements in a list
def find_duplicated(lst:list):
    a = []
    for i in lst:
        if lst.count(i)>1 and (i not in a):
            a.append(i)
    return a
print("# Case 2: find all duplicated elements in a list")
print(find_duplicated([1,2,3,4,2,1]))

# Case 3: Fibonacci in generator's version:
def Fibonacci(n):
    first, second = 1,1
    for _ in range(n):
        yield first 
        first , second = second, first + second

print("# Case 3: Fibonacci in generator's version:")
print(list(Fibonacci(5)))

# Case 4: Most frequent element
def mode(lst:list):
    a = []
    if not lst:
        return None
    else:
        max_element = max(lst, key=lambda v: lst.count(v))
        max_freq = lst.count(max_element)
        for x in lst:
            if lst.count(x) == max_freq:
                a.append(x)

    return list(set(a))

print("# Case 4: Most frequent element")
print(mode([1,1,2,2,3,2,1]))

# Case 5: Longest list
def max_len(*lst):
    print(max(lst, key=lambda v: len(v)))

print("# Case 5: Longest list")
max_len([1,2,3,4],[1,2,3],[4,5,6,7,8])

# Case 6 Print multiply table
def mul_table():
    for second in range(1,10):
        for first in range(1,second+1):
            print(f"{first} * {second} = {first*second}", end="\t")
        print('\n')
mul_table()

# Case 6: Paired couple
def couple(male_lst, female_lst):
    return list(zip(male_lst, female_lst))

result = couple(male_lst = ["John", "Charles", "Mike"], female_lst=["Vicky","Sunny","Dorcy"])
print("# Case 6: Paired couple")
print(result)

# Case 7: Random sampling

from random import randint, sample

def sampling(total_size, sample_size, min_value, max_value):
    lst = [randint(min_value,max_value) for _ in range(total_size)]
    sample_lst = sample(lst, sample_size)
    return sample_lst

print("# Case 7: Random sampling")
lst = sampling(100,20, 1, 500)
print(sum(lst)/ len(lst))
lst = sampling(100,50, 1, 500)
print(sum(lst)/ len(lst))

# Case 8: Shuffling
from random import shuffle
lst = [randint(0,50) for _ in range(100)]
shuffle(lst)
print(lst[:5])

# Case 9: Uniform
from random import uniform
def generate_uniform_point_pairs(x_size, y_range):
    x, y = [i for i in range(x_size)], [round(uniform(0,y_range),2) for _ in range(x_size)]
    print(list(zip(x, y))[:5])
    return x, y

from pyecharts.charts import Scatter
import pyecharts.options as opts
from pyecharts.commons.utils import JsCode
from pyecharts.faker import Faker

def draw_uniform_points():
    x, y = generate_uniform_point_pairs(x_size= 100, y_range = 10)
    # c = (Scatter()
    #      .add_xaxis(x)
    #      .add_yaxis("y-axis",y))
    # c.render()

    (
        Scatter()
            .add_xaxis(x)
            .add_yaxis(
            series_name="y-axis",
            y_axis=y,
            symbol_size=10,
            label_opts=opts.LabelOpts(is_show=True),
        )
            .set_series_opts()
            .set_global_opts(
                xaxis_opts=opts.AxisOpts(
                    type_="value",
                    splitline_opts=opts.SplitLineOpts(is_show=True)
                ),
                yaxis_opts=opts.AxisOpts(
                    type_="value",
                    axistick_opts=opts.AxisTickOpts(is_show=True),
                    splitline_opts=opts.SplitLineOpts(is_show=True),
                ),
                tooltip_opts=opts.TooltipOpts(is_show=True),
            )
            .render("pyecharts_html/uniform_points.html")
    )

    (
        Scatter()
            .add_xaxis(Faker.choose())
            .add_yaxis(
            "商家A",
            [list(z) for z in zip(Faker.values(), Faker.choose())],
            label_opts=opts.LabelOpts(
                formatter=JsCode(
                    "function(params){return params.value[1] +' : '+ params.value[2];}"
                )
            ),
        )
            .set_global_opts(
            title_opts=opts.TitleOpts(title="Scatter-多维度数据"),
            tooltip_opts=opts.TooltipOpts(
                formatter=JsCode(
                    "function (params) {return params.name + ' : ' + params.value[2];}"
                )
            ),
            visualmap_opts=opts.VisualMapOpts(
                type_="color", max_=150, min_=20, dimension=1
            ),
        )
            .render("pyecharts_html/scatter_multi_dimension.html")
    )

draw_uniform_points() # generating a render.html file
