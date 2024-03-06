# @Author: sushant Das

# @Date: 2021-03-05

# @Last Modified by: Author Name

# @Last Modified time: 2021-02-11 18:00:30

# @Title : Program to generate coupon code

from itertools import permutations

def coupon_generator(n):
    ls = [0,1,2,3,4,5,6,7,8,9]
    for i in list(permutations(ls, n)):
        print(*i)

if __name__=="__main__":
    coupon_generator(int(input("Enter the n distinct numbers : ")))

# def coupon_generator(coupon_nums):
#     coupon_len=len(coupon_nums)
#     print("All possible coupons that can be generated : ")
#     for i in list(permutations(coupon_nums, coupon_len)):
#         print(*i)


# if __name__=="__main__":
#     coupon_generator(input("Enter the n distinct numbers : "))