# 简单方法
x = range(10)
print(type(x))
sx = (x * x for x in range(10))
print(type(x))
'''
print(next(sx))
print(next(sx))
print(next(sx))
print(next(sx))
print(next(sx))
print(next(sx))
print(next(sx))
print(next(sx))
print(next(sx))
print(next(sx))
'''
for i in sx:
    print(i)
print('')

# 生成器实现fib数列
def fib(limit):
    n, a, b = 0, 0, 1
    while n < limit:
        yield b
        a, b = b, a + b
        n += 1
    return 'done'
for i in fib(10):
    print(i)
