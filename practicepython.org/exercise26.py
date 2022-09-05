import numpy
board = [
    [1,2,2],
    [1,1,2],
    [1,2,1]]

def line_match(board):
    for i in range(3):
        if board[i][0] == board[i][1] == board[i][2] and board[i][0] != 0:
            print(True)
