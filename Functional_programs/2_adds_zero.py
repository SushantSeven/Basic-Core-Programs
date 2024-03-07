# @Author: Sushant Das

# @Date: 2024-03-06

# @Last Modified by: Sushant Das

# @Last Modified time: 2021-02-11 18:00:30

# @Title : Find distinct combinations whose sum is equal to 0


from itertools import combinations

def zero_cal(numbers):
    ls = [i for i in list(combinations(numbers, 3)) if sum(i) == 0 if i not in ls ]
    print(ls)
    
if __name__=="__main__":
    n= int(input())
    numbers = [int(input()) for i in range(n)]
    zero_cal(numbers)