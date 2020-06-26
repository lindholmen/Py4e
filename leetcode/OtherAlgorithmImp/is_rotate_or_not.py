# 字符串 stringbook 旋转后得到 bookstring，写一段代码验证 str1 是否为 str2 旋转得到。

def is_rotation(s1, s2):
    if s1 == None or s2 == None:
        return False
    elif s1 in (s2+s2):
        return True
    else:
        return False

r = is_rotation('stringbook', 'bookstring')
print(r)  # True

r = is_rotation('greatman', 'maneatgr')
print(r)  # False


import re
pattern = re.compile(r'[\da-zA-Z]{6,20}')
print(pattern.fullmatch("qaz12"))
print(pattern.fullmatch("qaz12wsxedcrfvtgb67890942234343434"))
print(pattern.fullmatch('n0passw0Rd'))


