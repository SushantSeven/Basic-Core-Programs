# @Author: Sushant Das

# @Date: 2024-03-06

# @Last Modified by: Sushant Das

# @Last Modified time: 2021-02-11 18:00:30

# @Title : program to find the euclidian distance

import math

def eucli(x, y):
    print(math.sqrt(math.pow(x,2)+ math.pow(y, 2)))

if __name__=="__main__":
    x = int(input("Enter the value of x : "))
    y = int(input("Enter the value of y : "))
    eucli(x, y)