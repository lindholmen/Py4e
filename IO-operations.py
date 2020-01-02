#! /usr/bin/env python3

f = open("data.txt",'w')
#f.write("'r' This is the default mode. It Opens file for reading. 'w'	This Mode Opens file for writing. If file does not exist, it creates a new file.If file exists it truncates the file.'x'	Creates a new file. If file already exists, the operation fails.'a'	Open file in append mode. If file does not exist, it creates a new file.'t'	This is the default mode. It opens in text mode.'b'	This opens in binary mode.'+'	This will open a file for reading and writing (updating)\n")
#f.write("梅花香自苦寒来\n")
try:
    f.write("Make progress everyday\n")
    f.write("Today is March 1st 2019\n")
except:
    pass
finally:
    f.close()

# read() is to read all the text
f=open("data.txt")
wholetext = f.read()
print(wholetext)

f.seek(0) # curse to the beginning
# readlines() is to generate a list with each line as its item
textList = f.readlines()
textList.reverse()
textListAfterTrim = [x.rstrip() for x in textList]
print("the reversed text is:",textListAfterTrim)
print("Another way to get the list is to use split() ->",wholetext.split())

f.seek(0)
linetext = f.readline()
print(linetext)
# equals readline()
for line in f:# f is iterable!
    print("read line by line--->",line.rstrip())

f.close()
print("test if f is closed:", f.closed)

# using with

with open("data.txt") as with_file_opener:
    # call with_file_opener.__enter__() and __exit__() in order
    mydata = with_file_opener.read()

print("automatically closed:", with_file_opener.closed)
print(mydata)


# count = 0
# x = int(input("输入真数"))
# while x>1:
#     x //=2
#     count+=1
# print("approximate log2 is ",count)

# CREAT A FILE IF NOT EXIST AND ONLY ADD TO THE END
with open("data.txt","a") as with_file_opener:
    with_file_opener.write("Appending using 'a' !\n")

# R+ ONLY WORKS FOR EXISTING FILE and STARTS AT THE BEGINNING OF THE FILE
with open("data.txt","r+") as with_file_opener:
    with_file_opener.write("Adding using 'r+'!\n")
    with_file_opener.seek(70)
    with_file_opener.write("HAHAHA")


def statistics(filename):
    stat = {"lines":0,"words":0,"characters":0}
    with open(filename,"r") as filehandler:
        stat["words"] = len(filehandler.read().split())
        filehandler.seek(0)
        stat["lines"] = len(filehandler.readlines())
        filehandler.seek(0)
        stat["characters"] = len(filehandler.read())
        return stat


f = open("data.txt",'w')
f.write("Make progress everyday\n")
f.write("Today is March 1st 2019\n")
f.close()
print(statistics("data.txt"))



def find_and_replace(f, oldname,newname):
    with open(f,"r") as handler:
        story = handler.read()
        newstory = story.replace(oldname,newname)

    with open(f, "w") as handler2:
        handler2.write(newstory)

find_and_replace("story.txt","Bob","Alice")


def readlinesv2(f):
    line = f.readline()
    while line:
        yield line
        line = f.readline()

with open("data.txt","r") as f:
    for line in readlinesv2(f):
        print(line.strip())


# 序列化：json

import json
config ={"ip":'192.168.1.1', 'port': ['9100', '9101', '9102']}
with open("config.json","w+") as f:
    json.dump(config,f)

with open("config.json","r") as f:
    new_config_list = json.load(f)
print(type(new_config_list))


# dict和str相互转化
config_str = '{"ip": "192.168.1.1", "port": ["9100", "9101", "9102"]}'
config_dict = json.loads(config_str)
print(type(config_dict))
config_str = json.dumps(config)
print(type(config_str))