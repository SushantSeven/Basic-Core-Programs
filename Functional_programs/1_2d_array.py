# @Author: Sushant Das

# @Date: 2024-03-06

# @Last Modified by: Sushant Das

# @Last Modified time: 2021-02-11 18:00:30

# @Title : program to print a 2d array


def array_2d(m, n):
    ls = [[input("enter the element : ") for j in range(c)] for i in range(r)]
    print(ls)
    
if __name__ == '__main__':
    r , c = map(int , input(" Enter the number of rows and columns : ").split(" "))
    array_2d(r, c)


