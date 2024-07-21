board = [list(input()) for _ in range(3)]
winner = False
if any([all(board[i][j] == 'O' for j in range(3)) for i in range(3)]):
    winner = True
if any([all(board[j][i] == 'O' for j in range(3)) for i in range(3)]):
    winner = True
if all(board[i][i] == 'O' for i in range(3)):
    winner = True
if all(board[i][2-i] == 'O' for i in range(3)):
    winner = True
print('Jebb' if winner else 'Neibb')