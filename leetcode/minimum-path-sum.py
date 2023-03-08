class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        mat = [[0] * len(row) for row in grid]
        mat[0][:] = list(accumulate(grid[0], operator.add))
        for row_i in range(1, len(grid)):
            mat[row_i][0] = mat[row_i - 1][0] + grid[row_i][0]
            for col_i in range(1, len(grid[0])):
                mat[row_i][col_i] = min(mat[row_i - 1][col_i], mat[row_i][col_i - 1]) + grid[row_i][col_i]
        return mat[-1][-1]
    
class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        cost = [[0 for _ in range(len(row))] for row in grid]
        cost[0][:] = list(accumulate(grid[0], operator.add))

        for i in range(1, len(grid)):
            cost[i][0] = cost[i - 1][0] + grid[i][0]
            for j in range(1, len(grid[i])):
                cost[i][j] = min(cost[i - 1][j], cost[i][j - 1]) + grid[i][j]
        return cost[-1][-1]