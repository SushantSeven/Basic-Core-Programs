# @Author: Sushant Das

# @Date: 2024-03-04

# @Last Modified by: Sushant Das

# @Last Modified time: 2021-02-11 18:00:30

# @Title : prime factors


def prime_factors(n):
    factors = list()
    while n%2 == 0:
        factors.append(2)
        n = n//2

    for i in range(3,n+1, 2):
        while n%i == 0:
            factors.append(i)
            n = n//i
    if n > 2:
        factors.append(n)
    return factors

if __name__ == '__main__':
    result = prime_factors(int(input()))
    print(result)