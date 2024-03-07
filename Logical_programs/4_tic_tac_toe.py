# @Author: Sushant Das

# @Date: 2021-03-07

# @Last Modified by: Author Name

# @Last Modified time: 2021-02-11 

# @Title : Program to start and stop stopwatch


import random

# method to print the game board
def print_board(board, user):
    print(f"{board[0]} | {board[1]} | {board[2]}")
    print("--|---|--")
    print(f"{board[3]} | {board[4]} | {board[5]}")
    print("--|---|--")
    print(f"{board[6]} | {board[7]} | {board[8]}")
    print("\n")
    
    check_row_win(board, user)
    check_col_win(board, user)
    check_diag_win(board, user)
    check_tie(board)

# method to check if there is a win horizontally
def check_row_win(board, user):
    if board[0]==board[1]==board[2] and board[0]!="-":
        if user == "X":
            print(f"You Won!")
            exit()
        else:
            print("You lost! Better luck next time! ")
            exit()

    elif board[3]==board[4]==board[5] and board[3]!="-":
        if user == "X":
            print(f"You Won!")
            exit()
        else:
            print("You lost! Better luck next time! ")
            exit()

    elif board[6]==board[7]==board[8] and board[6]!="-":
        if user == "X":
            print(f"You Won!")
            exit()
        else:
            print("You lost! Better luck next time! ")
            exit()

# method to check if there is a win vertically
def check_col_win(board, user):
    if board[0]==board[3]==board[6] and board[0]!="-":
        if user == "X":
            print(f"You Won!")
            exit()
        else:
            print("You lost! Better luck next time! ")
            exit()

    elif board[1]==board[4]==board[7] and board[1]!="-":
        if user == "X":
            print(f"You Won!")
            exit()
        else:
            print("You lost! Better luck next time! ")
            exit()

    elif board[2]==board[5]==board[8] and board[2]!="-":
        if user == "X":
            print(f"You Won!")
            exit()
        else:
            print("You lost! Better luck next time! ")
            exit()

# method to chech if there is a win diagonaly
def check_diag_win(board, user):
    if board[0]==board[4]==board[8] and board[0]!="-":
        if user == "X":
            print(f"You Won!")
            exit()
        else:
            print("You lost! Better luck next time! ")
            exit()
    
    elif board[2]==board[4]==board[6] and board[2]!="-":
        if user == "X":
            print(f"You Won!")
            exit()
        else:
            print("You lost! Better luck next time! ")
            exit()
# method to check if there is a tie
def check_tie(board): 
    if "-" not in board:
        print("Its a tie !")
        exit()

#  method to place the player's move on the board
def move_placement(board, user):
    if user == 'X':
        print(f"Its your turn \n")
        move = int(input('Enter a number between 0 to 8 : '))
    else:
        print("Its computer's turn \n")
        move = random.randint(0, 8)
    if move>=0 and move<=8: #check if move is valid
        if board[move]=="-":  # check if another player is not already in the place
            board[move] = user
            print_board(board, user)
        else:
            print("Player already in place! try another move! ")
            return move_placement(board,user)
    else:
        print("Invalid move! ") # if the move is invalid call the move_placement function again
        return move_placement(board,user)

# method to start the game
def play_game():
    user = 'O'
    board = ["-","-","-","-","-","-","-","-", "-"]
    print_board(board,user)
    while True: # loop untill a player wins
        if user == 'O':
            user = 'X'
        else:
            user = 'O'
        move_placement(board, user) 

if __name__=="__main__":
    print("******Welcome to the Game!!!*****")
    play_game()
