# @Author: Sushant Das

# @Date: 2024-03-05

# @Last Modified by: Author Name

# @Last Modified time: 2021-02-11 18:00:30

# @Title : Gambler_program

import random 

def gamble(stake, goal):
    if goal < stake:
        print("Goal cannot be less than stake!")
        exit()
    
    win_count = lose_count = 0
    
    while stake<goal and stake>0:
        bet = random.randint(0,1)
        # if bet ==1:
        #     stake+=1
        #     win_count+=1 
        # else:
        #     stake-=1
        #     lose_count+=1
        stake += 1 if bet == 1 else -1; win_count += 1 if bet == 1 else 0; lose_count += 1 if bet != 1 else 0

        print(f"The gambler won! win percent is {(win_count/(win_count+lose_count))*100:.2f}%" if stake == goal else f"The gambler Lost! lose percent is {(lose_count/(win_count+lose_count))*100:.2f}%")

if __name__=="__main__":
    stake = int(input("Enter the stake value : "))
    goal = int(input("Enter the goal : "))
    gamble(stake, goal)

