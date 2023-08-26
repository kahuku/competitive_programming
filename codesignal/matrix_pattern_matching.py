# Roblox 2024 summer intern application
# given a matrix and a pattern, return True if the pattern is in the matrix
# pattern is a 2d array with numbers or letters
# matrix is a 2d array with numbers
# for corresponding indeces, the numbers must match
# letters in pattern are variables, can be any number but must be the same ([4, 2], [2, 1]) ([4, a], [b, 1]) is invalid
# so is ([4, 2], [2, 1]) and ([a, 2], [a, 1])

def is_match(matrix, pattern):
    d = {}
    s = set()
    for row in range(len(matrix)):
        for col in range(len(matrix[0])):
            if pattern[row][col] in ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']:
                if pattern[row][col] != matrix[row][col]:
                    return False
            else:
                if pattern[row][col] not in d:
                    if matrix[row][col] in s:
                        return False
                    d[pattern[row][col]] = matrix[row][col]
                    s.add(matrix[row][col])
                elif d[pattern[row][col]] != matrix[row][col]:
                    return False
    return True

def solution(matrix, pattern):
    for row in range(len(matrix) - len(pattern) + 1):
        for col in range(len(matrix[0]) - len(pattern[0]) + 1):
            sub = []
            for i in range(len(pattern)):
                sub.append(matrix[row + i][col:col + len(pattern[0])])
            if is_match(sub, pattern):
                return [row, col]
    return [-1, -1]