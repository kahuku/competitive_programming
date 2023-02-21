class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        grid = [[0] * len(row) for row in matrix]
        grid[0][:] = matrix[0]
        for row_i in range(1, len(matrix)):
            for col_i in range(len(matrix[row_i])):
                left_up = grid[row_i - 1][col_i - 1] if col_i else float('inf')
                right_up = grid[row_i - 1][col_i + 1] if col_i + 1 < len(matrix[row_i]) else float('inf')
                mid_up = grid[row_i - 1][col_i]
                grid[row_i][col_i] = matrix[row_i][col_i] + min(left_up, mid_up, right_up)
        return min(grid[-1])