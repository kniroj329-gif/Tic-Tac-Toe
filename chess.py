black_back = ["♜", "♞", "♝", "♛", "♚", "♝", "♞", "♜"]
black_pawns = ["♟", "♟", "♟", "♟", "♟", "♟", "♟", "♟"]
white_back = ["♖", "♘", "♗", "♕", "♔", "♗", "♘", "♖"]
white_pawns = ["♙", "♙", "♙", "♙", "♙", "♙", "♙", "♙"]
board = [ 
    black_back,
    black_pawns,
    [".", ".", ".", ".", ".", ".", ".", "."],
    [".", ".", ".", ".", ".", ".", ".", "."],
    [".", ".", ".", ".", ".", ".", ".", "."],
    [".", ".", ".", ".", ".", ".", ".", "."],
    white_pawns,
    white_back
]

n = 8
letters ="abcdefgh"
# for i in range(n):
#     print(8-i,end="  ")
#     for j in range(n):
#         print(board[i][j],end="  ")
#     print()
# print("   ",end="")
# for j in range(n):
#     print(letters[j],end="  ")

#created a function for displayinng board
def display_board (board):
    for i in range(n):
        print(8-i,end="  ")
        for j in range(n):
            print(board[i][j],end="  ")
        print()
    print("   ",end="")
    for j in range(n):
        print(letters[j],end="  ")
#moving pawn
def move(board,st_row,st_column,end_row,end_column):
    board[end_row][end_column] = board[st_row][st_column]
    board[st_row][st_column] = "."

move(board,1,1,2,1,)
display_board(board)
# board[2][1] = board[1][1]
# board[1][1] = "."
# display_board(board)




