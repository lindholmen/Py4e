#! /usr/bin/env python3
#using f-string, format and round(number you round, decimals)

print("How many kilometres you have run today?")
x = input()
print("Your {}km is {}mi ".format(x, float(x)*0.62))
print(f"Your {x}km is {float(x)*0.62}mi (this msg is print with F-string)")
# using the round functionality
# 1 km - 0.621371192 mile
print(f"Your {x}km is {round(float(x)*0.621371192,2)}mi")
