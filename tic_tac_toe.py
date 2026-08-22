board = ["1","2","3",
         "4","5","6",  
         "7","8","9",]

def display_board(board):
    print()
    print(board[0],"!",board[1],"!",board[2])
    print("-----------------")
    print(board[3],"!",board[4],"!",board[5])
    print("-----------------")
    print(board[6],"!",board[7],"!",board[8])
    print()
def check_winner(player):
    winning_combination = [
        [0, 1, 2],
        [3, 4, 5],
        [6, 7, 8],
        [0, 3, 6],
        [1, 4, 7],
        [2, 5, 8],
        [0, 4, 8],
        [2, 4, 6]
    ]
    for combination in winning_combination:
        if (board[combination[0]] == player and
         board[combination[1]] == player and
         board[combination[2]] == player): 
         return True 
    return False
player = "X"
while True:
    display_board(board)
    choice = int(input(f"player {player},choose a position(1-9) :" ))
    if board[choice-1] == str(choice):
     board[choice-1]=player
    else:
        print("the positon is already taken ") 
        continue
    if check_winner(player):
        display_board(board)
        print(f"player {player}, wins")
        break
    if all(position in ["X", "O"] for position in board):
        display_board(board)
        print("🤝 It's a draw!")
        break

    if player == "X":
        player = "O"
    else:
        player = "X"        










