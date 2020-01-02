from csv import reader
from csv import DictReader

# 每一行都是一个list
print("***************************************Using Reader***************************************")
with open("fighters.csv") as handler:
    csv_rows = reader(handler) # iterator
    table_header = next(csv_rows)# skip the table header or using list(csv_rows) to cast it to a list of lists!
    attr1, attr2, attr3 = table_header[0],table_header[1], table_header[2]
    for row in csv_rows:
        print(f"{attr1} {row[0]} is from the {attr2} {row[1]} with {attr3} of {row[2]}")

print("***************************************Using DictReader***************************************")

# 每一行都是一个OrderedDict, 放入dict的顺序和输出顺序是一致的， d=collections.OrderedDict()
# e.g. OrderedDict([('foo', 'python'), ('bar', 'spam')])
with open("fighters.csv") as handler:
    csv_dict_rows = DictReader(handler)
    # 表头已经不存在了！next(csv_dict_rows) 输出第一行真正数据！
    for row in csv_dict_rows:
        #print("rows:",row)
        #print("rows:",row.items())
        #print("rows:", list(row)) #等价于list(row.keys())
        items_list = list(row.items()) # Row 是一个多个tuple的iterable OrderedDict, 转型List 才能用 index
        print(f"{items_list[0][0]} {items_list[0][1]} is from the {items_list[1][0]} {items_list[1][1]} with {items_list[2][0]} {items_list[2][1]}"  )
        # or use print( ["Name"])

print("")

from csv import writer, DictWriter

with open("fighters.csv") as handler:
    csv_reader = reader(handler)
    with open("shouting_fighters.csv","w") as handler2:
        csv_writer = writer(handler2)
        for row in csv_reader:
            newlist = [ x.upper() for x in row]
            csv_writer.writerow(newlist)


def cm_to_inch(num):
    return num * 0.3937

with open("fighters.csv") as handler:
    csv_reader = reader(handler)
    table_header = next(csv_reader) # list
    table_header[2] = table_header[2].replace("cm", "inch") # replace不会改变原来string的值，必须assignment
    with open("inch_fighters.csv","w") as handler2:
        writer = DictWriter(handler2, fieldnames = table_header)
        writer.writeheader()
        for row in csv_reader:
            writer.writerow({table_header[0]: row[0],
                             table_header[1]: row[1],
                             table_header[2]: cm_to_inch(int(row[2]))})


with open("fighters.csv") as handler:
    csv_reader = DictReader(handler)

    table_header = list(next(csv_reader)) # list
    table_header_oldkey = table_header[2] # "height in cm"
    table_header[2] = table_header[2].replace("cm", "inch")  # replace不会改变原来string的值，必须assignment
    # ['Name', 'Country', 'Height (in inch)']

    handler.seek(0)
    csv_reader = DictReader(handler)


    with open("inch2_fighters.csv","w") as handler2:
         writer = DictWriter(handler2, fieldnames = table_header)
         writer.writeheader()
         for row in csv_reader:
             #row_content = list(row.items())
             writer.writerow({table_header[0]: row[table_header[0]],
                              table_header[1]: row[table_header[1]],
                              table_header[2]: cm_to_inch(int(row[table_header_oldkey]))})


import jsonpickle
class Thing():
    def __init__(self,name):
        self.name = name

    def __repr__(self):
        return f"I am {self.name}"

obj = Thing("Cool")

# from python obj to json
with open("jsonpicklefile.txt","w") as file:
    j = jsonpickle.encode(obj)
    file.write(j)

# convert json to python obj
with open("jsonpicklefile.txt","r") as file:
    content = file.read()
    decode_content =  jsonpickle.decode(content)
    print(type(decode_content))

import pickle
with open("pickle.txt","wb") as file:
    pickle.dump(obj, file)

with open("pickle.txt", "rb") as file:
    obj = pickle.load(file)
    print(obj) # I am Cool


# EXCERCISE update operation on the same file
'''
update_users("Grace", "Hopper", "Hello", "World") # Users updated: 1.
update_users("Colt", "Steele", "Boba", "Fett") # Users updated: 2.
update_users("Not", "Here", "Still not", "Here") # Users updated: 0.
'''

from csv import reader, writer
def update_users(oldfirst,oldlast,newfirst,newlast):
    with open("users.csv") as handler:
        csvrows = reader(handler)
        readinglist = list(csvrows)
        print(readinglist)
    with open("users.csv","w") as handler2:
        count = 0
        mywriter = writer(handler2)
        for row in readinglist:
            if row[0] == oldfirst and row[1] == oldlast:
                mywriter.writerow([newfirst,newlast])
                count +=1
            else:
                mywriter.writerow(row)
    return count
#print(update_users("Colt", "Steele", "Boba", "Fett"))

'''
delete_users("Grace", "Hopper") # Users deleted: 1.
delete_users("Colt", "Steele") # Users deleted: 2.
delete_users("Not", "Here") # Users deleted: 0.
'''

def delete_users(oldfirst,oldlast):
    with open("users.csv") as handler:
        csvrows = reader(handler)
        readinglist = list(csvrows)

    with open("users.csv","w") as handler2:
        count = 0
        mywriter = writer(handler2)
        for row in readinglist:
            if row[0] == oldfirst and row[1] == oldlast:
                count +=1
            else:
                mywriter.writerow(row)
    return "Users deleted: {}.".format(count)

print(delete_users("Colt", "Steele"))


###
description = []
list_of_labels_buying_computers = []
with open("sales.csv", "r") as handler:
    csv_reader = reader(handler)
    table_header = next(csv_reader)
    for row in csv_reader:
        column_size = len(row)
        list_of_labels_buying_computers.append(row[-1])
        row_dict = {}
        for i in range(column_size):
            row_dict[table_header[i]] = row[i]
        description.append(row_dict)

print(description)
print(list_of_labels_buying_computers)

import pickle

class MyObject:
    def __init__(self, x, y):
        self.x = x
        self.y = y

obj = MyObject(100, 200)
s_obj = pickle.dumps(obj)
print(type(s_obj)) #<class 'bytes'>
print(s_obj) #b'\x80\x03c__main__\nMyObject\nq\x00)\x81q\x01}q\x02(X\x01\x00\x00\x00xq\x03KdX\x01\x00\x00\x00yq\x04K\xc8ub.'
obj = pickle.loads(s_obj)
print(type(obj)) #<class '__main__.MyObject'>
print(obj)