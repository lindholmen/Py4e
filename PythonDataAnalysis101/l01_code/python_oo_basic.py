class MyClass(object):
    # 初始化函数
    def __init__(self, val):
        self.val = val

    def display(self, s):
        print('%s: %d' % (s, self.val))

m = MyClass(100)
print(m.val)
m.display('hello')
print('')

m2 = m
print(id(m))
print(id(m2))

fn = m.display
fn('hey')
