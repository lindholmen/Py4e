# coding: utf-8

# 初始化
s_a = set([1, 2, 3, 4, 5])
s_b = set([1, 1, 2, 2, 3, 4, 5])
print(s_a)
print(s_b)
print('')

# 获取长度
print(len(s_a))
print(len(s_b))
print('')

# 添加元素
s_a.add(6)
s_a.add(6)
s_a.update([5, 6, 7, 8, 9])
print(s_a)
print('')

# 删除元素
s_a.remove(8)
s_a.remove(9)
print(s_a)
print('')

# 判断元素是否存在
print(1 in s_a)
print(10 in s_a)
print('')

# 判断集合是否为空
s_a = set([])
if not s_a:
    print('set is empty')
else:
    print('set is not empty')
print('')

# 遍历
s_a = set([1, 2, 3, 4, 5])
for i in s_a:
    print(i)
print('')

# 集合操作
s_a = set([1, 2, 3, 4, 5])
s_b = set([4, 5, 6, 7, 8])
# 并集
print(s_a | s_b)
print(s_a.union(s_b))
# 交集
print(s_a & s_b)
print(s_a.intersection(s_b))
# 差集 s_a - (s_a and s_b)
print(s_a - s_b)
print(s_a.difference(s_b))
# 对称差
print(s_a ^ s_b)
print((s_a | s_b) - (s_a & s_b))
print(s_a.symmetric_difference(s_b))
