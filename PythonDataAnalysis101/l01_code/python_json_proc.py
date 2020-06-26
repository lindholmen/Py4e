import json

d = {'Python':100, 'C++':70, 'Basic':60, 'others':{'C':65, 'Java':50}}
jtxt = json.dumps(d)
dd = json.loads(jtxt)
print(jtxt)
print(dd)
print('')

# 非dict对象如何用json序列化？
class Student:
    def __init__(self, name, age, score):
        self.name = name
        self.age = age
        self.score = score

    def __str__(self):
        return '%s: %d, %d' % (self.name, self.age, self.score)

s = Student('Tom', 15, 85)
print(s)
print(s.__dict__)
# 方法1
jtxt = json.dumps(s, default = lambda obj: obj.__dict__)
print(jtxt)
def d2s(d):
    return Student(d['name'], d['age'], d['score'])
print(json.loads(jtxt, object_hook = d2s))
# 方法2
def s2d(s):
    return s.__dict__
jtxt = json.dumps(s, default = s2d)
print(jtxt)
