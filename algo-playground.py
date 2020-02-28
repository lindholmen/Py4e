#! /usr/bin/env python3

# 倒置输出int e.g. input 234 output 432 , 注意python 认为int 类型不止32位，而其他解释器认为int类型下最大的数据表示为2147483647=2^31-1，1位位符号位
input = -2147483648
num = abs(input)
output = 0
while num:
    mod_num = num%10
    output = mod_num + output*10
    num = int(num/10)
if num.bit_length() > 31:
    print("0 is output as it is out of index range")
else:
    print("output is:", output) if input>0 else print("output is:", -output)

# or using string
print("reverse using slicing", int(str(abs(input))[::-1]))
