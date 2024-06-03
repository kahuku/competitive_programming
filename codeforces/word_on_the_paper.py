import string

def transpose(matrix):
    rows, cols = 8, 8
    transposed = [[0 for _ in range(rows)] for _ in range(cols)]
 
    for i in range(rows):
        for j in range(cols):
            transposed[j][i] = matrix[i][j]
    
    return transposed

for _ in range(int(input())):
    grid = [list(input()) for _ in range(8)]
    row_counts = [8 - row.count('.') for row in grid]
    trans = transpose(grid)
    col_counts = [8 - col.count('.') for col in trans]
    if max(row_counts) >= max(col_counts):
        for row in grid:
            if ''.join(row) != '........':
                print(''.join([char for char in row if char in string.ascii_lowercase]))
    else:
        for col in trans:
            if ''.join(col) != '........':
                print(''.join([char for char in col if char in string.ascii_lowercase]))