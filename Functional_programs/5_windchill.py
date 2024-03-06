# @Author: Sushant Das

# @Date: 2024-03-04

# @Last Modified by: Sushant Das

# @Last Modified time: 2021-02-11 18:00:30

# @Title : Program to find windchill


import math
def windchill(t,v):
    print("Invalid input : ") if t > 50 or v > 120 or v < 3 else print(f"The windchill is {35.74 + 0.6215 * t - 35.75 * math.pow(v, 0.16) + 0.4275 * t * math.pow(v, 0.16) : .2f}\u00b0F")

if __name__=="__main__":
    t = float(input("Enter the temperature : "))
    v = float(input("Enter the wind speed : "))
    windchill(t,v)

