import random
    
# print board
# print(f"0 | 2 | 1")
    # print("--|---|--")
    # print(f"3 | 4 | 5")
    # print("--|---|--")
    # print(f"6 | 7 | 8")
# place the move

# switch user
# place the move
# check win lose tie

def print_board(board):
    # board[move] = user
    print(f"{board[0]} | {board[1]} | {board[2]}")
    print("--|---|--")
    print(f"{board[3]} | {board[4]} | {board[5]}")
    print("--|---|--")
    print(f"{board[6]} | {board[7]} | {board[8]}")

def move_placement(board):
    move = int(input('ENter a number between 0 to 9'))
    board[move] = 'X'
    print_board(board)


def play_game():
    board = ["-","-","-","-","-","-","-","-", "-"]
    while True:
        move_placement(board) 
play_game()


# def print_board(board):
#     print(f"{board[0]} | {board[1]} | {board[2]}")
#     print("--|---|--")
#     print(f"{board[3]} | {board[4]} | {board[5]}")
#     print("--|---|--")
#     print(f"{board[6]} | {board[7]} | {board[8]}")

# def move_placement(board, user):
#     while True:
#         move = int(input('Enter a number between 1 to 9: ')) - 1
#         if 0 <= move <= 8 and board[move] == "-":
#             board[move] = user
#             break
#         else:
#             print("Invalid move. Please try again.")
    
#     print_board(board)

# def check_winner(board, user):
#     # Check rows, columns, and diagonals for a win
#     win_conditions = [[0, 1, 2], [3, 4, 5], [6, 7, 8], [0, 3, 6], [1, 4, 7], [2, 5, 8], [0, 4, 8], [2, 4, 6]]
#     for condition in win_conditions:
#         if all(board[pos] == user for pos in condition):
#             return True
#     return False

# def play_game():
#     board = ["-", "-", "-", "-", "-", "-", "-", "-", "-"]
#     print_board(board)
#     current_player = 'X'

#     while True:
#         print(f"Player {current_player}'s turn:")
#         move_placement(board, current_player)
#         if check_winner(board, current_player):
#             print(f"Player {current_player} wins!")
#             break
#         if "-" not in board:
#             print("It's a tie!")
#             break
#         current_player = 'O' if current_player == 'X' else 'X'

# play_game()
