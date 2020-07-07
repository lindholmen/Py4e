import time

# method 1: 假定一个零点基准，偏移长度换算为按秒的数值型
# method 2: 9 个整数组成的元组 struct_time 表示的时间
seconds = time.time()
print("seconds:",seconds)

local_time = time.localtime(seconds)
print("local_time:", local_time)
str_time = time.asctime(local_time)
print("local time in string:", str_time)
format_time = time.strftime('%Y-%m-%d %H:%M:%S',local_time)
print("formated time:", format_time)


str_to_struct = time.strptime(format_time,'%Y-%m-%d %H:%M:%S')
print("str_to_struct:", str_to_struct)

#     %Y  年
#     %m  月 取值 [01,12]
#     %d  天 取值 [01,31]
#     %H  小时 取值 [00,23]
#     %M  分钟 取值 [00,59]
#     %S  秒 取值 [00,61]

from datetime import date, datetime, time, timedelta
#date：日期类，包括属性年、月、日及相关方法
# time：时间类，包括属性时、分、秒等及相关方法
#datetime：日期时间，继承于 date，包括属性年、月、日、时、分、秒等及相关方法，其中年月日必须参数
today = date.today()
print("today:",today, " with type ", type(today))

str_date = date.strftime(today, "%Y / %m / %d")
print("str_date:",str_date)

str_to_date = datetime.strptime(str(today), '%Y-%m-%d')
print("str_to_date:", str_to_date)
print("type:", type(str_to_date))
print("convert to base class:", type(str_to_date.date()))

right_now = datetime.now()
print("Right now:" ,right_now)

str_time =  datetime.strftime(right_now,'%Y-%m-%d %H:%M:%S')
print("str_time:", str_time)


str_to_time = datetime.strptime('2020-02-22 15:12:33','%Y-%m-%d %H:%M:%S')
print("str_to_time:", str_to_time)


# timedelta


# 案例：计算还有几天是女朋友生日
import re
def calculate_bdays_left(birthday:str) -> int:
    splits = re.split(r'[-.\s+/]',birthday)
    splits = [s for s in splits if s]
    if len(splits)<3:
        raise ValueError("Wrong input format")
    splits = splits[:3]
    birthday = datetime.strptime("-".join(splits),'%Y-%m-%d')
    today = date.today()
    # 相减的两个时间，不能一个为 date 类型，一个为 datetime 类型，所以必须将birthday转为date型
    delta = birthday.date() - today
    return delta.days

print(calculate_bdays_left("2020  12  25"))


import calendar
from datetime import date
today = date.today()
year_calendar_str = calendar.calendar(today.year)
print(f"{today.year}年的日历图：\n{year_calendar_str}\n")

import calendar
from datetime import date
mydate = date.today()
month_calendar_str = calendar.month(mydate.year, mydate.month)
print(f"{mydate.year}年-{mydate.month}月的日历图：\n{month_calendar_str}\n")

# 判断闰年 leap year
import calendar
from datetime import date

mydate = date.today()
is_leap = calendar.isleap(mydate.year)
print_leap_str = "%s年是闰年\n" if is_leap else "%s年不是闰年\n"
print(print_leap_str % mydate.year)

# 判断月有几天
import calendar
from datetime import date

mydate = date.today()
weekday, days = calendar.monthrange(mydate.year, mydate.month)
print(f'{mydate.year}年-{mydate.month}月的第一天是那一周的第{weekday}天')
print(f'{mydate.year}年-{mydate.month}月共有{days}天\n')

# 月的第一天
from datetime import date
mydate = date.today()
month_first_day = date(mydate.year, mydate.month, 1)
print(f"当月第一天:{month_first_day}\n")

# 月最后一天
from datetime import date
import calendar
mydate = date.today()
_, days = calendar.monthrange(mydate.year, mydate.month)
month_last_day = date(mydate.year, mydate.month, days)
print(f"当月最后一天:{month_last_day}\n")