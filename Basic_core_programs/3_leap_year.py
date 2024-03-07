# @Author: Sushant Das

# @Date: 2024-03-04

# @Last Modified by: Sushant Das

# @Last Modified time: 2021-02-11 18:00:30

# @Title : Leap Year


def leap_year(year):
    if year%400==0 or year%4 == 0 and year%100!=0:
        return True
    else:
        return False

if __name__  == '__main__':
    result = leap_year(int(input("Enter the year ")))
    if result is True:
        print("leap year")
    else:
        print("Not a leap year")