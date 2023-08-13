# given matrix
# return max sum of elements of rhombus with radius r
def solution(matrix, radius):
    m = float('-inf')
    for row in range(radius - 1, len(matrix) - radius + 1):
        for col in range(radius - 1, len(matrix[0]) - radius + 1):
            indeces = get_indeces(radius, row, col)
            m = max(m, sum([matrix[i][j] for i, j in indeces]))
    return m

def get_indeces(r, center_x, center_y):
    indeces = []
    rows = 0
    for col in range(-r, r):
        for row in range(rows):
            indeces.append((center_x - col, center_y + row))
            if rows != 0:
                indeces.append((center_x - col, center_y - row))
        if col >= r:
            rows -= 1
        else:
            rows += 1
    return indeces