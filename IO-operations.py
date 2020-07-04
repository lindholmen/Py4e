#! /usr/bin/env python3

#f = open("data.txt",'w')
#f.write("'r' This is the default mode. It Opens file for reading. 'w'	This Mode Opens file for writing. If file does not exist, it creates a new file.If file exists it truncates the file.'x'	Creates a new file. If file already exists, the operation fails.'a'	Open file in append mode. If file does not exist, it creates a new file.'t'	This is the default mode. It opens in text mode.'b'	This opens in binary mode.'+'	This will open a file for reading and writing (updating)\n")
#f.write("梅花香自苦寒来\n")
# try:
#     f.write("Make progress everyday\n")
#     f.write("Today is March 1st 2019\n")
# except:
#     pass
# finally:
#     f.close()

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


# f = open("data.txt",'w')
# f.write("Make progress everyday\n")
# f.write("Today is March 1st 2019\n")
# f.close()
# print(statistics("data.txt"))



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


from collections import defaultdict
import re

regex = re.compile(r'\s+')
d = defaultdict(int)
with open("data.txt", "r+") as f:
    for line in f:
        clean_line = line.strip()
        if clean_line:
            lst = regex.split(clean_line)
            for word in lst:
                d[word] +=1

d = sorted(d.items(), key=lambda x: x[1], reverse = True)
print(d)


#返回所有目录下相通后缀名的

import os

def find_file(work_dir,extension='py'):
    lst = []
    for filename in os.listdir(work_dir): #拿到所有的文件
        splits = os.path.splitext(filename)
        ext = splits[1] # 拿到扩展名
        if ext == '.'+extension:
            lst.append(filename)
    return lst

r = find_file('.','csv')
print(r) # 返回所有目录下的 csv 文件

# 批量重命名后缀
def batch_rename(work_dir, old_ext, new_ext):
    """
    传递当前目录，原来后缀名，新的后缀名后，
    """
    for filename in os.listdir(work_dir):
        # 获取得到文件后缀
        split_file = os.path.splitext(filename)
        file_ext = split_file[1]
        if old_ext == file_ext: # 定位后缀名为old_ext 的文件
            newfile = split_file[0] + new_ext # 修改后文件的完整名称
            print("newfile:", newfile)
            # 实现重命名操作
            os.rename(
                os.path.join(work_dir, filename),
                os.path.join(work_dir, newfile)
            )
    print("完成重命名")
    #print(find_file('.','new_ext'))

batch_rename(".", ".old_ext", ".new_ext")



# 获取目录下文件的修改时间
import os
from datetime import datetime

print(f"当前时间：{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")

def get_modify_time(indir):
    for root, dirname, files in os.walk(indir):  # 循环目录和子目录
        for file in files:
            whole_file_name = os.path.join(root, file)
            modify_time = os.path.getmtime(whole_file_name) # 1581164725.991523，这种时间格式太不人性化
            nice_show_time = datetime.fromtimestamp(modify_time) # 转化为人性化的时间显示格式：2020-02-08 20:25:25.991523
            print('文件 %s 最后一次修改时间：%s' %(file,nice_show_time))
            
get_modify_time("./leetcode")