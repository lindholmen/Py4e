class FunctionalList():

    def __init__(self, values=None):  # 初始化
        if values is None:
            self.values = []
        else:
            self.values = values

    def __len__(self):
        return len(self.values) + 10  # 故意多加10个

    def __getitem__(self, key):
        if type(key) == slice:  # 如果传入的key是一个slice类，则这是一个切片访问
            start = key.start
            stop = key.stop + 1
            if key.stop == None:
                stop = -1
            if key.start == None:
                start = 0
            return self.values[start:stop]
        else:
            return str(self.values[key]) * 2  # 故意多输出2次

    def __setitem__(self, key, value):
        self.values[key] = str(value) + 'haha'  # 故意都给转成str，再加haha字样

    def __delitem__(self, key):
        pass
        # del self.values[key]#就是故意不去删

    def __iter__(self):  # 用于迭代器，之所以列表、字典、元组等可以进行for循环，是因为类型内部定义了 __iter__
        #         pass
        return iter(self.values)

    def __reversed__(self):
        return reversed(self.values)

    def append(self, value):  # 非魔术方法
        self.values.append(value)


l1 = list(range(10))
o1 = FunctionalList(l1)
print(len(o1))  # 调用的是__len__
print(o1[0:9])


# __cmp__(self, other) __cmp__ 是最基本的用于比较的魔术方法。
# 它实际上实现了所有的比较符号(<,==,!=,etc.)，
# 但是它的表现并不会总是如你所愿(比如，当一个实例与另一个实例相等是通过一个规则来判断，
# 而一个实例大于另外一个实例是通过另外一个规则来判断)。
# 如果 self < other 的话 __cmp__ 应该返回一个负数，当 self == other 的时候会返回0 ，而当 self > other 的时候会返回正数。
# 通常最好的一种方式是去分别定义每一个比较符号而不是一次性将他们都定义。
# 但是 __cmp__ 方法是你想要实现所有的比较符号而一个保持清楚明白的一个好的方法。

# __eq__(self, other) 定义了等号的行为, == 。

# __ne__(self, other) 定义了不等号的行为, != 。

# __lt__(self, other) 定义了小于号的行为， < 。

# __gt__(self, other) 定义了大于等于号的行为， >= 。

# 示例
class myclass():
    def __init__(self, num):
        self.num = num
        print('被__init__')

    def __del__(self, ):
        print('被__del__')

    def __eq__(self, other):
        if type(other) == int:
            return True if self.num == other else False
        else:
            print('can\'t compare with other datatype except int', )


c1 = myclass(3)
print(c1 == 3)

# 你可以通过魔术方法控制控制使用 isinstance() 和 issubclass() 内置方法的反射行为。这些魔术方法是:

# __instancecheck__(self, instance)

# 检查一个实例是不是你定义的类的实例

# __subclasscheck__(self, subclass)

# 检查一个类是不是你定义的类的子类


# 可以调用的对象
# Python中，方法也是一种的对象。这意味着他们也可以被传递到方法中就像其他对象一样。
# __call__可以让类的实例的行为表现的像函数一样，被调用
# 将一个函数当做一个参数传到另外一个函数中等等。这是一个非常强大的特性让Python编程更加舒适甜美。

# 魔法函数 __call__(self, [args...])

# __call__允许一个类的实例像函数一样被调用。
# 实质上说，这意味着 x() 与 x.__call__() 是相同的。
# 注意 __call__ 参数可变。这意味着你可以定义 __call__ 为其他你想要的函数，无论有多少个参数。

class callableInstance():

    def __init__(self, x, y):
        self.x, self.y = x, y

    def __call__(self, ):
        self.x, self.y = self.y, self.x
        # 调用时交换对象


c1 = callableInstance(1, 5)  # 执行 __init__,赋值x,y
print(c1.x, c1.y)
c1()  # 执行 __call__,交换变量变换
print(c1.x, c1.y)


