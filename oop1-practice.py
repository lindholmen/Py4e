

class User:

    myflag = True
    somelist = [0,1,2]
    active_user = 0 # 一般用于创建全局的变量 independent of detailed instances info
    def logout(self):
        User.active_user -= 1
        return f"{self.first} has logged out"


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



    def setNameMangling(self, something):
        self.__message = something
    def getNameMangling(self):
        return self.__message

    @classmethod # 不依赖任何instance.
    def display_active_users(cls):
        return f'there are actually {cls.active_user} active users'

    @classmethod
    def from_string(cls,data_str): #  it just enhances the functionality of our User class, allowing us to pass a single string argument and create a user from it
        first, last, age = data_str.split(',') # equals first , last, age = 'a','b', '23'
        return cls(first,last,age)

    def __repr__(self):
        return f"{self.first} {self.last} with age {self.age}"


user1 = User("Joe","Ali", 23)
user2 = User("Bana", "sMITH", 13)
user3 = User("Slark","lOPEZ",19)
print("the user's name is", user1.displayName())
print("the user's initials is", user1.initials())

# name mangling
user1.setNameMangling("Hi!")
print(dir(user1))
print("Directly access name mangling:", user1._User__message)
print("Retrieve name mangling:", user1.getNameMangling())

# class attribute
#User.myflag = False # 全局修改，
# 实际user1, user2, user3 是referece class attribute,除非user1.is_meaningful = True, then only user1 changes.
print(user1.myflag, user2.myflag)
print(user1.somelist, user2.somelist)
print(id(user1.myflag), id(user2.myflag), id(User.myflag))
print("change user1's myflag attirbute to False:")
user1.myflag = False
print(user1.myflag, user2.myflag, User.myflag)
print("change user2's somelist attirbute:")
user2.somelist.append(100)
print(user1.somelist, user2.somelist, User.somelist)

print(f"there are {User.active_user} active users")
print(user3.logout())


#class method
print(User.display_active_users())
user4 = User.from_string("Jason,Bourne,30") # dict.fromKeys(["a","b","c"],None)创建dict一样{'a':None, "b":None,"c":None}
print("created user by classmethod :") # __repr__ overload
print(user4)
print(user1)
print(user2)


class Pet:
    allowed = ['cat', 'dog']
    def __init__(self, name, spe):
        if spe not in Pet.allowed:
            raise ValueError(f"cannot have {spe} pet")
        self.name = name
        self.spe = spe

pet1 = Pet("Kitty", "cat")
pet2 = Pet("james", "dog")
Pet.allowed.append("fish")
print(id(pet1.allowed),id(pet2.allowed), id(Pet.allowed)) # refering to the same class attr
pet1.allowed.append("tiger")
print(pet1.allowed)
print(pet2.allowed)
print(Pet.allowed)
print(id(pet1.allowed),id(pet2.allowed), id(Pet.allowed)) # refering to the same class attr

# getter and setter as decorators:
class Rectangle:
    def __init__(self, width, height):
        self._width = None
        self._height = None
        # now we call our accessor methods to set the width and height
        self.width = width
        self.height = height

    def __repr__(self):
        return 'Rectangle({0}, {1})'.format(self.width, self.height)

    @property
    def width(self):
        return self._width

    @width.setter
    def width(self, width):
        if width <= 0:
            raise ValueError('Width must be positive.')
        self._width = width

    @property
    def height(self):
        return self._height

    @height.setter
    def height(self, height):
        if height <= 0:
            raise ValueError('Height must be positive.')
        self._height = height


#r1 = Rectangle(0, 10) # will have ValueError 因为这里设置的是其proxy property, 而其setter中有判断逻辑
r2 = Rectangle(10,5)
print(r2)
r2.height = 99 # call height.setter
print(r2)
