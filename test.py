class User:

    myflag = True
    mystr = "ok"
    mynum = 1

    somelist = [0, 1, 2]

    def __init__(self, first,last,age): # self refers to the current class instance
        self.first = first
        self.last = last
        self.age = age




user1 = User("Joe","Ali", 23)
user2 = User("J.R.", "Smith", 13)
user3 = User("William","Lopes",19)

# class attribute
print(user1.myflag, user2.myflag) # True True
print(user1.somelist, user2.somelist)  # [0, 1, 2] [0, 1, 2]
print(id(user1.myflag), id(user2.myflag), id(User.myflag)) # 4492567424 4492567424 4492567424
print("change user1's myflag attribute to False:")
user1.myflag = False
print(user1.myflag, user2.myflag, User.myflag) # False True True
print(id(user1.myflag), id(user2.myflag), id(User.myflag)) # 4492567392 4492567424 4492567424


print("change user2's somelist attirbute:")
user2.somelist.append(100)
# user2.somelist = ['a','b','c'] 这个只修改user2的attribute
print(user1.somelist, user2.somelist, User.somelist) # [0, 1, 2, 100] [0, 1, 2, 100] [0, 1, 2, 100]
print(id(user1.somelist), id(user2.somelist), id(User.somelist)) # 4521416904 4521416904 4521416904

print("change user1's mystr attirbute:")
print(id(user1.mystr), id(user2.mystr), id(User.mystr)) #4495067320 4495067320 4495067320
user1.mystr = "no"
print(user1.mystr, user2.mystr, User.mystr) # no ok ok
print(id(user1.mystr), id(user2.mystr), id(User.mystr)) # 4495553904 4495067320 4495067320

print("change user1's mynum attirbute:")
print(id(user1.mynum), id(user2.mynum), id(User.mynum)) # 4375365568 4375365568 4375365568
user1.mynum = 99
print(user1.mynum, user2.mynum, User.mynum) #99 1 1
print(id(user1.mynum), id(user2.mynum), id(User.mynum)) # 4375368704 4375365568 4375365568