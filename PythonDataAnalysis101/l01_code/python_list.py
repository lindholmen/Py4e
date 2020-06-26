# 初始化列表
li = [1, 2, 3, 'abc', 4.5, [2, 3, 4], {1:'one'}]

# 获取长度
print(len(li))
print('')

# 根据索引读写
print(li[0])
print(li[3])
print(li[-1])
print('')

# 添加元素
li = [1, 2, 3]
li.append('a')
li.append('b')
print(li)
li.append([4, 5, 6])
print(li)
li = [1, 2, 3]
li.extend([4, 5, 6])
print(li)
print('')

# 删除元素
li = [1, 2, 3, 4, 5]
li.pop()
print(li)
del(li[0])
del(li[1])
print(li)
print('')

# 元素是否存在
li = [1, 2, 3, 4, 5]
print(1 in li)
print(6 in li)
print('')

# 列表是否为空
li = []
if not li:
    print('Empty')
else:
    print('Not empty')
print('')

# 字符串
s = 'abcdefg'
li = list(s)
li[4] = 'E'
li[5] = 'F'
print(li)
s = ''.join(li)
print(s)
print('')

# 遍历
li = [1, 2, 3]
for i in li:
    print(i)
for i in range(len(li)):
    print(li[i])
