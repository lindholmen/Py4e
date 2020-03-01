# name = input('input your name:\n')
# if name == "jack":
#     print("boy")
# elif name == "lucy":
#     print("girl")
# else:
#     print("NA")
from random import randint, choice

if 0:
    print("0 is evaluated as true")
else:
    print("0 is evaluated as false")

if None:
    print("None is evaluated as true")
else:
    print("None is evaluated as false")

an_empty_string = ""
if an_empty_string:
    print("empty string is evaluated as true")
else:
    print("empty string is evaluated as false")

for i in range (1,10,2): #([start, end),interval )
    print("this is old number：", i)

for i in range(5):
    print("from 0 by default:", i)

numberRg = range(1,10)
print("print out the range class object:", numberRg)
print("use range class to create list:",list(numberRg))


rows = 0
emoji_string = ""
while rows <= 8:
    for i in range(0, rows+1):
        emoji_string = emoji_string + "\U0001f600" # alternative = print（emoji_string* (rows +1))
    print(emoji_string)
    emoji_string = ""
    rows = rows + 1

# msg = input("how are you？")
# while (msg != "stop"):
#     msg = input(f"{msg}\n")

def guess(secret_num):
    num = int(input("input a number between 1 and 10:"))
    while num != secret_num:
        if num < secret_num:
            print("too low")
            num = int(input())
        else:
            print("too high")
            num = int(input())
    print("Right!")


guess(randint(1,10))
user_choice = input("wanna play again?")
while user_choice == "y":
    guess(randint(1,10))
    user_choice = input("wanna play again?")
