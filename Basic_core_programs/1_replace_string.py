# @Author: Sushant Das

# @Date: 2024-03-04

# @Last Modified by: Sushant Das

# @Last Modified time: 2021-02-11 18:00:30

# @Title : User Input and Replace String Template “Hello <<UserName>>, How are you?”



def hello(name):
    while True:
        if len(name)>=3:
            print(f"Hello {name}, How are you?")
            return False
        else:
            print("The name must have atlleast 3 char.")
            name = input("Enter your name")
            return hello(name)

if __name__ == '__main__':
    name = input()
    hello(name)

