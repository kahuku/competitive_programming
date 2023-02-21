class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        if obstacleGrid[0][0] or obstacleGrid[-1][-1]:
            return 0
        grid = [[0] * len(row) for row in obstacleGrid]
        grid[0][0] = 1
        blocked = False
        for i in range(1, len(grid[0])):
            if obstacleGrid[0][i] == 1:
                blocked = True
            if not blocked:
                grid[0][i] = 1

        for row_i in range(1, len(grid)):
            if obstacleGrid[row_i][0]:
                grid[row_i][0] = 0
            else:
                grid[row_i][0] = grid[row_i - 1][0]
            for col_i in range(1, len(grid[0])):
                if obstacleGrid[row_i][col_i] == 1:
                    grid[row_i][col_i] = 0
                else:
                    grid[row_i][col_i] = grid[row_i - 1][col_i] + grid[row_i][col_i - 1]
        return grid[-1][-1]