# @Author: Sushant Das

# @Date: 2021-03-05

# @Last Modified by: Author Name

# @Last Modified time: 2021-02-11 

# @Title : Program to start and stop stopwatch

import time

def stopwatch():
    while True:
        start = input("Type 'START' to start the stopwatch :")
        if start == 'START':
            start_time = time.time()
            end = input('type end to stop : ')
            if end == 'end':
                end_time = time.time()
                elapsed_time = end_time - start_time
                print(f"Elapsed time: {elapsed_time:.2f} seconds")
                return False
            else:
                print('Please ennter correct command ')
        else:
            print('Please ennter correct command ')

if __name__=='__main__':
    stopwatch()
