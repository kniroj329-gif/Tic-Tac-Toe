#creating board
black_back = ["♜", "♞", "♝", "♛", "♚", "♝", "♞", "♜"]
black_pawns = ["♟", "♟", "♟", "♟", "♟", "♟", "♟", "♟"]
white_back = ["♖", "♘", "♗", "♕", "♔", "♗", "♘", "♖"]
white_pawns = ["♙", "♙", "♙", "♙", "♙", "♙", "♙", "♙"]
black_pieces = ["♜", "♞", "♝", "♛", "♚", "♝", "♞", "♜", "♟"]
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
#displaying the board
display_board(board)
#moving pawn
def move(board,st_row,st_column,end_row,end_column):
     piece = board[st_row][st_column]
     if piece == "♙":
         #for normal forward
         if ((st_row == 6 and end_row == st_row -2 and board[st_row-1][st_column]==".") or  (end_row == st_row -1)) and end_column == st_column and board[end_row][end_column]==".":
                       board[end_row][end_column] = piece
                       board[st_row][st_column] = "."
        #for diagonal capture
         elif board[end_row][end_column] in black_pieces:
            if end_row == st_row -1 and end_column == st_column-1 or end_column == st_column:
                 board[end_row][end_column] = piece
                 board[st_row][st_column] = "."
         else:
          print("invalid move")   
     
#conoverting position
def convert_position(position):
    column = letters.index(position[0])
    row = 8-int(position[1])
    return row, column 

#getting input to move the pieces
start = ((input("\nenter starting square : ")))
st_row, st_column = convert_position(start)
end = (input("enter ending square : "))
end_row, end_column = convert_position(end)
move(board,st_row,st_column,end_row,end_column)
display_board(board)







