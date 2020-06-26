class Base:
    pass

class MyClass(Base):
    def run(self):
        print('MyClass run')
        
class MyClass2(Base):
    def run(self):
        print('MyClass2 run')

m = MyClass()
print(isinstance(m, MyClass))
print(issubclass(MyClass2, Base))
print('')

# 多态
m2 = MyClass2()
m.run()
m2.run()
print('')

def duck(d):
    d.run()

class Man:
    def run(self):
        print('man run')

class Monkey:
    def run(self):
        print('monkey run')

duck(Man())
duck(Monkey())
