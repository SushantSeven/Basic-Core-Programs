# @Author: Sushant Das

# @Date: 2024-03-04

# @Last Modified by: Sushant Das

# @Last Modified time: 2021-02-11 18:00:31

# @Title : Harmonic Number

def harmonic(n):
    if n <= 0:
        print('N must be greater than 0')
        n = int(input("Enter the Number: "))
        return harmonic(n)
    else:
        res = 0
        for i in range(1, n + 1):
            res += 1 / i
        return (1 / res)

if __name__ == '__main__':
    num = int(input("Enter the Number: "))
    result = harmonic(num)
    print(result)
