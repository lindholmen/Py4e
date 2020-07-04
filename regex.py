import re

# 等价两种写法
# 1. phone_regex = re.compile(r"\d{3}-\d{3}-\d{4}")
# re.search(str)
# 2. re.search(r"\d{3}-\d{3}-\d{4}",str)


#分组
print("String: 'Work Number is 416-123-6868. Home number is 000-123-8888.'")
phone_regex = re.compile(r"(\d\d\d)-(?P<second>\d\d\d-\d\d\d\d)") # give a name to the second group
# find first match, return None if not found
mo = phone_regex.search("Work Number is 416-123-6868. Home number is 000-123-8888.")
mo_for_all = phone_regex.findall("Work Number is 416-123-6868. Home number is 000-123-8888.")
print("group1 as the first group:",mo.group(1)) #用group()获得匹配regex的全部内容
print("group2 as the second group:",mo.group("second"))
print("return the entire matching string:",mo.group(0), ", same as mo.group():", mo.group())

print("return multiple groups:",mo.groups()) # tuple
print("return all matches in a list of tuples:", mo_for_all)
#不分组
phone_regex = re.compile(r"\d\d\d-\d\d\d-\d\d\d\d")
mo_for_all = phone_regex.findall("Work Number is 416-123-6868. Home number is 000-123-8888.")
print("return all matches in a list only:", mo_for_all)

#carrots cost dollars
print("")
phone_regex = re.compile(r"^\d\d\d-\d\d\d-\d\d\d\d$") # the entire string must match, otherwise return None
mo = phone_regex.search("416-123-6868")
print("carrots cost dollars to match the entire string:",mo.group())
mo = re.fullmatch(r"\d{3}-\d{3}-\d{4}","416-123-6868") # the entire string must match
print("Version 2: using fullmatch to check the entire string:",mo.group())

#wildcard . (except newline)
print("")
phone_regex = re.compile(r".\d\d-\d\d\d-\d\d\d\d")
mo_for_all = phone_regex.findall("Work Number is 416-123-6868. Home Number is 000-123-8888.")
print("using a wild card:", mo_for_all)
phone_regex = re.compile(r"Number is (.*)") # match anything except newline
mo = phone_regex.search("Work Number is 416-123-6868\nHome Number is 000-123-8888")
print("using a dot star:", mo.group())
phone_regex = re.compile(r"Number is (.*)",re.DOTALL) # match anything re.I 忽略大小写|
mo = phone_regex.search("Work Number is 416-123-6868\nHome Number is 000-123-8888")
print("using a dot star AND DOTALL:", mo.group())

# greedy and non-greedy
print("")
phone_regex = re.compile(r"Number is (.*)\.")
mo = phone_regex.search("Work Number is 416-123-6868. Home Number is 000-123-8888.")
print("greedy:", mo.group())
phone_regex = re.compile(r"Number is (.*?)\.")
mo = phone_regex.search("Work Number is 416-123-6868. Home Number is 000-123-8888.")
print("non-greedy:", mo.group())

# 用去替换的文字可以是来自于group的内容 \1表示第一组的内容
print("")
phone_regex = re.compile(r"Number is (\d\d\d-\d\d\d-\d)\d*")
print(phone_regex.findall("Work Number is 416-123-6868. Home Number is 000-123-8888."))
print(phone_regex.sub(r"Number is \1****","Work Number is 416-123-6868. Home Number is 000-123-8888."))

# complex regex using re.VERBOSE 忽略regex中空格
phoneRegex = re.compile(r'''
    (\d{3}|\(\d{3}\))?  # area code
    (\s|-|\.)?          # separator
    (\d{3})               # first 3 digits
    (\s|-|\.)           # separator
    (\d{4})               # last four digits
    (\s*(ext|x|ext.)\s*\d{2,5})?
    ''', re.VERBOSE| re.I|re.DOTALL)
mo = phoneRegex.search("My number is (555) 222 8888 Ext. 7655")
print("group()>",mo.group())
print("group1>", mo.group(1))
print("group3>", mo.group(3))

# 做一个regex版本的strip,对一个给出的字符串，执行strip(str)操作后，首尾都不能有str的字符
def RegexStrip(str,strippedChars= ''):
    if strippedChars == '':
        regex = re.compile(r'^\s*(.*\S)\s*$',re.DOTALL)
        return regex.sub(r"\1", str)
    else:
        #regex = re.compile(r'^['+ strippedChars + r']*(.*[^'+ strippedChars + r'])[' + strippedChars + r']*$',re.DOTALL)
        regex = re.compile(fr"^[{strippedChars}]*(.*[^{strippedChars}])[{strippedChars}]*$",re.DOTALL)
        return regex.sub(r'\1',str)

print(RegexStrip("bcWWW acBHabc",'abc')) # WWW acBH

# match URL
url_regex = re.compile(r'(https?)://(www\.[A-za-z-]{2,256}\.[a-z]{2,6})([-a-zA-Z0-9@:%_\+.~#?&//=]*)')
match = url_regex.search("https://www.my-website.com/bio?data=blah&dog=yes")
print(f"Protocol: {match.group(1)}")
print(f"Domain: {match.group(2)}")
print(f"Everything Else: {match.group(3)}")
print(match.groups())
print(match.group())

# matching binary number in a string:

def parse_bytes(inputstr):
    myregex = re.compile(r"\b[01]+\b")
    mo = myregex.findall(inputstr)
    return list(mo)

print(parse_bytes("1010101011 123 23 010010101"))
print(parse_bytes("101230101011 23"))
print(parse_bytes("012"))


# exercise
def parse_date(inputstr):
    regex = re.compile(r"^(?P<d>\d\d)[/.,](?P<m>\d\d)[/.,](?P<y>\d\d\d\d)$")
    mo = regex.search(inputstr)
    # print(mo.group("d"))
    # print(mo.group("m"))
    # print(mo.group("y"))
    if mo:
        return {"d":mo.group("d"),"m":mo.group("m"),"y":mo.group("y")}
    return None

print(parse_date("20/10/1987"))

# exercise for email
email_regex = re.compile(r"""
    ^([a-z0-9_\.-]+)
    @
    ([a-z0-9\.-]+)
    \.
    ([a-z\.]{2,6})$
""",re.VERBOSE|re.I)

mo = email_regex.search("Nick@gmail.com")
print(mo.groups())

# exercise for substitution
regex = re.compile(r"(Mr.|Ms.|Mrs.) ([a-z])[a-z]+",re.I)
text = "Last night Mr. Holm murdered Mrs. Jackson and Ms. Jane"
mo = regex.findall(text)
if mo:
    print(mo)
result1 = regex.sub("\g<1> \g<2>***", text)
result2 = regex.sub(r"\1\2***", text)
print(result1, " and ",result2)


# swapping name
titles = [
    "Significant Others (1987)",
    "Tales of the City (1978)",
    "The Days of Anna Madrigal (2014)",
    "Mary Ann in Autumn (2010)",
    "Further Tales of the City (1982)",
    "Babycakes (1984)",
    "More Tales of the City (1980)",
    "Sure of You (1989)",
    "Michael Tolliver Lives (2007)"
]

titles.sort()
print(titles)
# 给组取名
myregex = re.compile(r"(?P<title>[\w]+) \((?P<year>\d{4})\)")
newtitle = []
for element in titles:
    #注意这里引用不同组的写法
    newtitle.append(myregex.sub(r"\g<year> - \g<title>", element))
print(newtitle)

people = ['Dr. Christopher Brooks', 'Dr. Kevyn Collins-Thompson', 'Dr. VG Vinod Vydiswaran', 'Dr. Daniel Romero']

def split_title_and_name(person):
    title = person.split()[0]
    lastname = person.split()[-1]
    return f'{title} {lastname}'

#print(list(map(split_title_and_name, people)))


myregex = re.compile(r"[^\w ]")
text = myregex.sub(" ","i am a F!! No, I, that is not me.")
text = text.lower()
X = filter(None,text.split(" "))
word_cnt = {}
for word in filter(None,text.split(" ")):
    word_cnt.setdefault(word,0)
    word_cnt[word] = word_cnt[word] +1

print(word_cnt)


# finditerator
s = '山东省潍坊市青州第1中学高三1班'
pat = '1'
r = re.finditer(pat, s)
for i in r:
    print(i)


s = 'That'
pat = r't'
r = re.finditer(pat,s,re.I)
for i in r:
    print(i.span())


# Split
s = 'This,,,   module ; \t   provides|| regular ; '
words = re.split('[,\s;|]+',s)
print("words:", words)