# 初始化
d = {'a':1, 2:'b', 'c':3, 4:'d'}
print(d)
print('')

# 获取长度
print(len(d))
print('')

# 根据key读写
d['a'] = 100
d[4] = 'dd'
print(d)
print('')

# 添加元素
d['e'] = 5
d[6] = 'f'
print(d)
print('')

# 删除元素
d = {'a':1, 2:'b', 'c':3, 4:'d'}
del(d['a'])
del(d[2])
print(d)
print('')

# 判断key是否存在
d = {'a':1, 2:'b', 'c':3, 4:'d'}
if 'a' in d:
    print('a in d')
if 2 in d:
    print('2 in d')
if not ('x' in d):
    print('x not in d')
print('')

# 判断字典是否为空
d = {}
if not d:
    print('d is empty')
print('')

# 遍历
d = {'a':1, 2:'b', 'c':3, 4:'d'}
for k in d.keys():
    print(str(k) + ': ' + str(d[k]))
for k, v in d.items():
    print(str(k) + ': ' + str(v))
