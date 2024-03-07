# @Author: Sushant Das

# @Date: 2024-03-04

# @Last Modified by: Sushant Das

# @Last Modified time: 2021-02-11 18:00:30

# @Title : Power of 2

def power(n):
    while True:
        if n>31:
            print('The value of N must be less than 31')
            break
        else:
            for i in range(n+1):
                print(f'2^{i} = {2**i}')
            return False
    power(int(input("Enter the Number ")))
    
if __name__=='__main__':
    power(int(input("Enter the Number ")))
