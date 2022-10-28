
########################### TIC-TAC-TOE #########################################
import random

import time



# board = [ [" "," "," "],
#           [" "," "," "],
#           [" "," "," "] ]

player = "X" # starting player

# games_range = ["0","1","2","3","4","5","6","7","8"]

def print_board(board):
    board1 = ["|".join(board[0]),"|".join(board[1]),"|".join(board[2])]
    print("\n".join(board1))
    

def print_rules():
    board =  [[0,1,2],
              [3,4,5],
              [6,7,8]]
    
    # print("Board Outline :")
    print(board[0][0],"|",board[0][1],"|",board[0][2])
    print(board[1][0],"|",board[1][1],"|",board[1][2])
    print(board[2][0],"|",board[2][1],"|",board[2][2])
    # print("Enter any no. between 0-8 to mark on the board")

def mark(player,var,board):
    if var == "0":
        board[0][0] = player
    elif var == "1":
        board[0][1] = player
    elif var == "2":
        board[0][2] = player
    elif var == "3":
        board[1][0] = player
    elif var == "4":
        board[1][1] = player
    elif var == "5":
        board[1][2] = player
    elif var == "6":
        board[2][0] = player
    elif var == "7":
        board[2][1] = player
    elif var == "8":
        board[2][2] = player

def switch_turn(player):
    if player == "X":
        return "O"
    if player == "O":
        return "X"

def check_diagonal(board):
    if board[0][0] == board[1][1] == board[2][2] != " ":
        return True
    if board[0][2] == board[1][1] == board[2][0] != " ":
        return True
    else :
        False
def check_hoz(board):
    if board[0][0] == board[0][1] == board[0][2] != " ":
        return True
    if board[1][0] == board[1][1] == board[1][2] != " ":
        return True
    if board[2][0] == board[2][1] == board[2][2] != " ":
        return True
    else :
        False
def check_vertical(board):
    if board[0][0] == board[1][0] == board[2][0] != " ":
        return True
    if board[0][1] == board[1][1] == board[2][1] != " ":
        return True
    if board[0][2] == board[1][2] == board[2][2] != " ":
        return True
    else :
        False


def check_win(board):
    if check_diagonal(board) or check_hoz(board) or check_vertical(board): 
        return True

def hvh():
    games_range = ["0","1","2","3","4","5","6","7","8"]
    board = [ [" "," "," "],
          [" "," "," "],
          [" "," "," "] ]
    global player
    print_rules()
    while (" " in board[0] or " " in board[1] or " " in board[2] and check_win(board) != True):
        print("options :" ," ".join(games_range))
        marking = input("{player}'s turn :")
        while marking not in games_range:
            marking = input("Sorry Invalid Input, {player} goes again :")
        
        games_range.remove(marking)
        mark(player,marking,board)
        print_board(board)
        print("\n")
        if check_win(board):
            print(f"\n{player} Wins")
            break
    
        player = switch_turn(player)
    
    if check_win(board):
        print("")
    elif " " not in board[0] and " " not in board[1] and " " not in board[2]:
        print("\nIt's a Draw")


def hvc():
    games_range = ["0","1","2","3","4","5","6","7","8"]
    board = [ [" "," "," "],
          [" "," "," "],
          [" "," "," "] ]
    human_marker = input("choose ur marker (X/O):")
    global player
    print_rules()
    while (" " in board[0] or " " in board[1] or " " in board[2] and check_win(board) != True):
    
        if player == human_marker:
            print("options :" ," ".join(games_range))
            marking = input(f"{player}'s turn :")
            while marking not in games_range:
                marking= input(f"Sorry Invalid Input, {player} goes again :")
            games_range.remove(marking)
            mark(player,marking,board)
            print_board(board)
            print("\n")
        
    
        
        else:
            time.sleep(0.8)
            marking = random.choice(games_range)
            games_range.remove(marking)
            mark(player,marking,board)
            print_board(board)
            print("\n")
        
        
    
        
        if check_win(board):
            print(f"\n{player} Wins")
            break
    
        player = switch_turn(player)
    if check_win(board):
        print("")
    elif " " not in board[0] and " " not in board[1] and " " not in board[2]:
        print("\nIt's a Draw")
    

def cvc():
    games_range = ["0","1","2","3","4","5","6","7","8"]
    board = [ [" "," "," "],
          [" "," "," "],
          [" "," "," "] ]
    global player
    print_rules()
    while (" " in board[0] or " " in board[1] or " " in board[2] and check_win(board) != True):
        time.sleep(1)
        marking = random.choice(games_range)
        if player == "X":
            print(f"X makes a move to {marking}")
        elif player == "O":
            print(f"O makes a move to {marking}")
        games_range.remove(marking)
        mark(player,marking,board)
        print_board(board)
        
        if check_win(board):
            print(f"\n {player} Wins")
            break
    
        player = switch_turn(player)
    
    if check_win(board):
        print("")
    elif " " not in board[0] and " " not in board[1] and " " not in board[2]:
        print("\nIt's a Draw")
    
############ EXECUTION ##################

def TTT():
    u = input("Enter mode (cvc/hvc/hvh) :")
    if u == "cvc":
        cvc()
        ans = input("Go Again? (yes/no):")
        if ans == "yes":
            TTT()
        
    elif u == "hvc":
        hvc()
        ans = input("Go Again? (yes/no):")
        if ans == "yes":
            TTT()
    elif u == "hvh":
        hvh()
        ans = input("Go Again? (yes/no):")
        if ans == "yes":
            TTT()

TTT()
