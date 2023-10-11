class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        s = []
        for r in range(len(matrix)):
            for c in range(len(matrix[0])):
                cell = matrix[r][c]
                if cell == 0:
                    s.append([r, c])
        for r, c in s:
            for ro in range(len(matrix)):
                matrix[ro][c] = 0
            for co in range(len(matrix[0])):
                matrix[r][co] = 0
        return matrix
        