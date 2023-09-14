n = int(input())
board = [list(input()) for _ in range(n)]
row_possible = True
col_possible = True

highest_row = 0
for row in board:
    highest_row = max(highest_row, row.count('1'))

highest_col = 0
for col in zip(*board):
    highest_col = max(highest_col, col.count('1'))

total_1s = 0
for row in board:
    total_1s += row.count('1')

if (n - highest_row) + (total_1s - highest_row) > n:
    row_possible = False

if (n - highest_col) + (total_1s - highest_col) > n:
    col_possible = False

if row_possible and col_possible:
    print('+')
else:
    print('-' if row_possible else '|')