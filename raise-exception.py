#! /usr/bin/env python3



#raise ValueError("something wrong with value")
#raise NameError("name is not correct")

def foo(text, color):
    colors = ("yellow","blue","red")

    if type(text) is not str or type(color) is not str:
        raise TypeError("input must be string")
    if color not in colors:
        raise ValueError("color is not invalid color")
    print(f"text is {text} and color is {color}")

try:
    foo("hi","red")

except ValueError:
    print("value error")


def divide():
    while True:
        try:
            real_input1 = input("enter a number:")
            if real_input1 == "quit":
                break
            real_input2 = input("enter another number:")
            num1 = int(real_input1)
            num2 = int(real_input2)

            #import pdb; pdb.set_trace() # 如果在pycharm里面调试就不要这个！！几个命令：l:show line, n:next, c: continue, p: print

            result = num1/num2
        except ValueError as err: # or except (ValueError,ZeroDivisionError ) as err
            print(err)
            print("not a number")
            continue
        except ZeroDivisionError as err:
            print(err)
            print("0 cannot be the second number")
        else:
            print(f"{num1} divided by {num2} is {result}")
        finally:
            print("runs no matter what") # even they have continue!!

divide()