# @Author: Sushant Das

# @Date: 2024-03-06

# @Last Modified by: Sushant Das

# @Last Modified time: 2021-02-11 18:00:30

# @Title : Program to find the roots of a quadric equation

import math

def quad(a,b,c):
    delta = b*b - 4*a*c
    # if delta<0:
    #     print("There are no real roots!")
    # elif delta == 0:
    #     print(f"The root of the given equation {a}x^2 + {b}x + {c} is {-b / (2 * a)}")
    # else:
    #     print(f"The roots of the given equation {a}x^2 + {b}x + {c} are {(-b - math.sqrt(delta)) / (2 * a)} and {(-b + math.sqrt(delta)) / (2 * a)}") 
    print("There are no real roots!") if delta < 0 else (print(f"The root of the given equation {a}x^2 + {b}x + {c} is {-b / (2 * a)}") if delta == 0 else print(f"The roots of the given equation {a}x^2 + {b}x + {c} are {(-b - math.sqrt(delta)) / (2 * a)} and {(-b + math.sqrt(delta)) / (2 * a)}"))

if __name__=="__main__":
    a, b, c = map(int, input(" Enter the three numbers").split(" "))
    quad(a,b,c)

