# @Author: Sushant Das

# @Date: 2024-03-04

# @Last Modified by: Sushant Das

# @Last Modified time: 2021-02-11 18:00:30

# @Title : Flip Coin and print percentage of Heads and Tails

import random
def flip(n):
    heads = 0
    tails = 0
    for i in range(n):
        flip = random.uniform(0, 1)
        if flip<=0.5:
            heads += 1
        else:
            tails += 1
    print(f"The percentage of heads is {(heads/n)*100}%")
    print(f"The percentage of tails is {(tails/n)*100}%")

if __name__=='__main__':
    flip(int(input("ENter the number of flips")))

