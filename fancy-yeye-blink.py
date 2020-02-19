import termcolor
import random
#from termcolor import colored

# print(dir(termcolor))
#help(termcolor)

# use colored(text, color=None, on_color=None, attrs=None)
list_color = ["grey", "red", "green", "yellow", "blue", "magenta", "cyan", "white"]
list_on_color = ["on_grey","on_red","on_green","on_yellow", "on_blue", "on_magenta","on_cyan","on_white"]

list_gong = ["龚爷爷屌炸天", "敬业福拿到手软的崇明霸主","叼下有92年精锐男人","扫福最牛崇明异端儿", "五福早就他娘合成的上海滩霸主","学霸张克星"]


for i in range(0,1000):
    random_color = random.choice(list_color)
    random_on_color = random.choice(list_on_color)
    while random_on_color.endswith(random_color):
        random_color = random.choice(list_color)
        random_on_color = random.choice(list_on_color)

    text = termcolor.colored(random.choice(list_gong), color = random_color , on_color= random_on_color, attrs=["bold"])
    print(text, end=" ")


# for i in range(10):
#     termcolor.cprint(i, 'magenta', end= " ")

