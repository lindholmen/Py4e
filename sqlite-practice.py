import sqlite3

conn = sqlite3.connect("my_friends.db") # 如果没有就创建
# create a cursor
c = conn.cursor()

#cursor executes
# first time run this code:
#cmd_create_table = "CREATE TABLE friends(firstname TEXT, lastname TEXT, closeness INTEGER );"
#c.execute(cmd_create_table)

#bad insertion
# cmd_insert = '''INSERT INTO friends(firstname, lastname , closeness ) VALUES ("Zhanghuan","Gong", "666");'''
# c.execute(cmd_insert)

#good insertion
# new_data = ("shenye","Gong",888)
cmd_better_insert = f"INSERT INTO friends VALUES (?,?,?)"
# c.execute(cmd_better_insert, new_data)

# insert many, or use for loop
#bulk_data = [("niubi","Gong",777), ("zong","Gong",999), ("yiduaner","Gong",1000)]
#c.executemany(cmd_better_insert,bulk_data)

# select all
# c.execute("select * from friends")
# for result in c:
#     print(result)

# fetch all
c.execute("select * from friends where closeness > 700 order by closeness")
print(c.fetchall())

# using ? as a placeholer for variable to query
u = ("Yeye",)
query = f"SELECT * FROM friends WHERE firstname=?"
c.execute(query,u)
print("# using ? as a placeholer for single variable to query :", c.fetchall())

query = f"SELECT * FROM friends WHERE firstname=? and lastname =?"
c.execute(query,("Yeye","Gong"))
print("# using ? as a placeholer for multiple variable to query for multiple ",c.fetchall())

#connection to commit
conn.commit()

#close the connection
conn.close()