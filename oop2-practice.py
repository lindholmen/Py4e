
import copy
class Animal:
    existed = True
    def make_sound(self, sound):
        print("this animal makes the soud of",sound)

    def __init__(self,first,last,age):
        self.first = first
        self.last = last
        self._age = max(age, 0)

    def __repr__(self):
        return f"Pet info: {self.first} {self.last}"

    # The property is just so that it appears that you are retrieving/changing the value of a property rather than calling a method.
    @property
    def age(self):
        return f"{self._age} Years Old"

    # the point of a property is to give you a shortcut to change single properties in a class.
    @age.setter
    def age(self, newage):
        if newage > 0:
            self._age = newage

    @property
    def full_name(self):
        return self.first + " " + self.last

    @full_name.setter
    def full_name(self, newname):
        self.first, self.last = newname.split(" ")

    def running(self):
        print("animal running!")




class Dog(Animal):
    def __init__(self, first, last, age, breed, toy):
        self.first = first
        self.last = last
        self.age = age
        self.breed = breed
        self.toy = toy
    def running(self):
        print("dog running!")


my_dog = Dog("Dallas", "M", 10,"chiwawa","toyX")
print(isinstance(my_dog, Animal))
my_dog.make_sound("Wow!")
my_dog.existed = False
print(my_dog.existed)

# age is a proxy for _age 针对父类animal如此，然后继承下来
# age is actually a function, but used like a property
# getter and setter by property has the same name!
print("dog age through property age:", my_dog.age) # 调用父类方法！！！！
my_dog.age = 20
print("dog age has been updated through setter:", my_dog.age)
print("my dog's full name:", my_dog.full_name)
my_dog.full_name = "Lebron James"
print("my dog's new full name:", my_dog.full_name)
# object's __dict__property:
print("my dog's info:", my_dog.__dict__)
#
#
#
class Cat(Animal):
    def __init__(self, first, last, age, breed, toy):
        # intro to super(),no more self
        super().__init__(first,last,age)
        self.breed = breed
        self.toy = toy

    def play(self):
        print(f"{self.full_name} plays with {self.toy}")

    def running(self):
        print("cat running!")


my_cat = Cat("Lucy", "J", 7,"Scottish","String")
print(my_cat)
my_cat.play()


# poly 多态
#重载
my_dog.running()
my_cat.running()
# 对于一个变量，我们只需要知道它是Animal类型，无需确切地知道它的子类型，就可以放心地调用running()方法，而具体调用的running()方法是作用在Animal、Dog、Cat
# 由运行时该对象的确切类型决定，这就是多态真正的威力：调用方只管调用，不管细节，
def double_running(animal):
    animal.running()
    animal.running()
# 而当我们新增一种Animal的子类时，只要确保run()方法编写正确，不用管原来的代码是如何调用的。这就是著名的“开闭”原则：
# 对扩展开放：允许新增Animal子类；
# 对修改封闭：不需要修改依赖Animal类型的double_running等函数。
class Lion(Animal):
    def running(self):
        print("lion running!")

double_running(Animal("1","2",3))
double_running(Dog("1","2",3,"4","5"))
double_running(Cat("1","2",3,"4","5"))
double_running(Lion("1","2",3))




class User:


    active_user = 0 # 一般用于创建全局的变量 independent of detailed instances info

    # The first argument of every class method, including init, is always a reference to the current instance of the class.
    # By convention, this argument is always named self. In the init method, self refers to the newly created object;
    # in other class methods, it refers to the instance whose method was called.
    def __init__(self, first,last,age): # self refers to the current class instance
        self.first = first
        self.last = last
        self.age = age
        User.active_user += 1
    def displayName(self):
        return self.first + " " + self.last
    def initials(self):
        return self.first[0] +"."+ self.last[0] + "."

    def logout(self):
        User.active_user -= 1
        return f"{self.first} has logged out"

    @classmethod # 不依赖任何instance.
    def display_active_users(cls):
        return f'there are actually {cls.active_user} active users'

    @classmethod
    def from_string(cls,data_str): #  it just enhances the functionality of our User class, allowing us to pass a single string argument and create a user from it
        first, last, age = data_str.split(',') # equals first , last, age = 'a','b', '23'
        return cls(first,last,age)

    def __repr__(self):
        return f"{self.first} {self.last} aged {self.age}"

    def __len__(self):
        return self.age

    def __add__(self, other):
        if isinstance(other,User):
            return User(self.first+"-"+other.first, last= self.last, age = 0)
        else:
            return "you cannot do that"

    def __mul__(self, other):
        return [copy.copy(self) for i in range(other)]

class Moderator(User):

    total_moderator = 0
    def __init__(self,first,last, age, community):
        super().__init__(first,last,age)
        self.community = community
        Moderator.total_moderator += 1

    def remove_post(self):
        return f"{self.displayName()} removed a post from {self.community} community"

    def __repr__(self):
        return f"{self.first} {self.last} with age {self.age} in the community of {self.community}"

    @classmethod
    def display_active_moderators(cls):
        return f"there are currently {cls.total_moderator} active moderator users"


print(User.display_active_users())
u1 = User("Tom", "Hanks", 35)
u2 = User("jack", "Skin", 36)
u3 = User("wolf", "Hanky", 37)
print("self defined magic method:",len(u3))
print(u2+u3) # __add__
newlist = u1 * 2
newlist[1].last = "Nikky"
print(newlist) # __mul__

print(User.display_active_users())
Dirk = Moderator("Dirk","Norwitski", 39, "basketball")
Dirk2 = Moderator("Dirk2","Norwitski2", 40, "nba")

print(User.display_active_users())
print(Moderator.display_active_moderators())

class A:
    def __init__(self, name):
        self.name = "Mr." + name

    def greeting(self):
        print(f"i am {self.name}, king of the A")


class B:
    def __init__(self, name):
        self.name = "Mrs." + name

    def greeting(self):
        print(f"i am {self.name}, king of the B")

    def shouting(self):
        print(f"i am shouting!")

class C(A,B): # 对于父类都有的方法，从左到右的顺序，只执行A class.
    def __init__(self,name):
        super().__init__(name = name)
        #B.__init__(self,name = name)

    def greeting(self):
        print(f"i am {self.name}, king of the C")
        super().greeting()

multiple_inheritance_Obj = C("Jason B")
multiple_inheritance_Obj.greeting() # will call for class A's method when using super().greeting()
# three ways to find out MRO method resolution order
print(C.__mro__)
print(C.mro())
help(C) # super() will refer to whatever is next in the MRO. in this case it is A.
# 但是依然会可以访问父类的方法！！
multiple_inheritance_Obj.shouting()

class Device():
    def __init__(self,name, connected_by):
        self.name = name
        self.connected_by = connected_by
        self.connected = True

    def __str__(self):
        return f"Device {self.name!r} ({self.connected_by})"

    def disconnected(self):
        self.connected = False

    def reconnect(self):
        self.connected = True

class Printer(Device):
    def __init__(self,name,connected_by, capacity):
        super().__init__(name, connected_by)
        self.capacity = capacity
        self.remaining = capacity

    def __repr__(self):
        return f"{super().__str__()} with remaining {self.remaining} pages"

    def print(self,pages):
        if not self.connected:
            print("not connected")
            return
        print(f"Printed....remaining {self.remaining-pages}")
        self.remaining -= pages

    def disconnected(self):# overload
        self.connected = False
        print("Printer class object disconnected")

    def __mul__(self, other): # magic method
        return [copy.copy(self) for i in range(other)]

printer = Printer("Canon","USB",100)
print(printer)
printers = printer * 3
print(printers)
printer.print(40)
printer.disconnected()
printer.print(40)
print(printer)
printer.reconnect()
printer.print(40)
print(printer)

# CLASS COMPOSITION = a class is composed of multiple objects, "has relationship" rather than "is"
print("")
print("**************class composition***************")

class Bookshelf:
    def __init__(self,*books):
        self.books = books

    def __str__(self):
        return f"This bookshelf has {len(self.books)} books"

class Book():
    def __init__(self,name):
        self.name = name

    def __str__(self):
        return f"This book is {self.name}"


book1 = Book("Harry Potter")
book2 = Book("12 secerets")
print(book1)
print(book2)
bookshelf = Bookshelf(book1,book2)
print(bookshelf)

