#%%

record = ('Dave', 'dave@example.com', '773-555-1212', '847-555-1212')
name, email, *phone_numbers = record
print(phone_numbers)

records = [
    ('foo', 1, 2),
    ('bar', 'hello'),
    ('foo', 3, 4),
]
def something(x,y):
    return x+y

for tag, *parameters in records:
    if tag == 'foo':
        print("foo:",something(*parameters)) # to unpack
    elif tag == 'bar':
        print("bar",parameters) # still packing form

line = 'nobody:*:-2:-2:Unprivileged User:/var/empty:/usr/bin/false'
group = line.split(":")


#%% 队列deque 类
from collections import deque


def search(lines, pattern, history=5):
    previous_lines = deque(maxlen=history)
    for line in lines:
        if pattern in line:
            yield line, previous_lines
        previous_lines.append(line)

# Example use on a file
with open('data/somethingtoread.txt',"r") as file:
    for line, prevlines in search(file, 'Python', 5):
        for pline in prevlines:
            print("previous five lines:",pline, end='')
        print("searched pattern sentence:", line, end='')
        print('-' * 20)

# find the largest n elements in list：
print(' ' * 20)
print("find the largest/smallest n elements in list")
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

# PriorityQueue
class PriorityQueue:
    def __init__(self):
        self._queue = []
        self._index = 0

    def push(self, item, priority):
        heapq.heappush(self._queue, (-priority, self._index, item))# put the whole tuple as an item into the queue
        # as heappop will always pop the smallest item, so with with smallest value of (-priority) will be popped!
        # if two items have the same priority, then index could ensure they still can be compared!
        self._index += 1

    def pop(self):
        return heapq.heappop(self._queue)[-1]

class Item():
    def __init__(self,name):
        self.name = name

    def __repr__(self):
        return f"{self.name}"

q = PriorityQueue()
q.push(Item('foo'), 1)
q.push(Item('bar'), 5)
q.push(Item('spam'), 4)
q.push(Item('grok'), 1)
print(q.pop())
print(q.pop())
print(q.pop())
print(q.pop())


# defaultdict - one key multiple values:
from collections import defaultdict
d = defaultdict(list)
#自动初始化每个 key 刚开始对应的值
d['a'].append(1)
d['a'].append(2)
d['b'].append(4)
print("list:",d)
s = defaultdict(set)
s['a'].add(1)
s['a'].add(2)
s['b'].add(4)
print("set：",s)


# ordereddict
# OrderedDict 内部维护着一个根据键插入顺序排序的双向链表。
# 每次当一个新的元素插入进来的时候， 它会被放到链表的尾部。对于一个已经存在的键的重复赋值不会改变键的顺序。
from collections import OrderedDict

d = OrderedDict()
d["B"] = 2
d["A"] = 1
d["C"] = 3
d["C"] = 0
for key in d:
    print(f"key:{key}, value:{d[key]}")

# want to the min and max price
prices = {
    'ACME': 45.23,
    'AAPL': 612.78,
    'IBM': 205.55,
    'HPQ': 37.20,
    'FB': 10.75
}
#zip 翻转key-value pair
price_list = list(zip(prices.values(),prices.keys()))

print(min(price_list))
print(max(price_list))
print(sorted(price_list))
print("股价从小到大的股票代码：", sorted(prices, key = lambda x:prices[x]))
print("股价最高股：",max(prices,key=lambda x:prices[x]))

prices = {
    'ACME': 45.23,
    'FB': 45.23
}
print("key相同时看值大小：max - ",max(zip(prices.values(),prices.keys())))
print("key相同时看值大小：min - ",min(zip(prices.values(),prices.keys())))

# 查找两字典的相同点
a = {
    'x' : 1,
    'y' : 2,
    'z' : 3
}

b = {
    'w' : 10,
    'x' : 11,
    'y' : 2
}

print(a.keys()-b.keys())
print(a.keys() &  b.keys())

# 删除序列相同元素并保持顺序
def dudupe(items):
    myset = set()
    for item in items:
        if item not in myset:
            myset.add(item)
            yield item

a = [1, 5, 2, 1, 9, 1, 5, 10]
for i in dudupe(a):
    print("value in the list:",i)

# 这个方法仅仅在序列中元素为 hashable 的时候才管用。 如果你想消除元素不可哈希（比如 dict 类型）的序列中重复元素的话:
a_nonhashable = [ {'x':1, 'y':2}, {'x':1, 'y':3}, {'x':1, 'y':2}, {'x':2, 'y':4}]
def dudupe_nonhashable(items, func=None):
    myset = set()
    for item in items:
        val = item if func is None else func(item)
        if val not in myset:
            myset.add(val)
            yield item
print(list(dudupe_nonhashable(a_nonhashable,lambda e: (e["x"],e['y']))))



