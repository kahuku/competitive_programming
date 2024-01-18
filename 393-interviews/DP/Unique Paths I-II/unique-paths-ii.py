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
    
class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        if obstacleGrid[0][0] or obstacleGrid[-1][-1]:
            return 0

        m, n = len(obstacleGrid), len(obstacleGrid[0])
        mat = [[0 for _ in range(n)] for _ in range(m)]
        
        for i in range(len(mat[0])):
            if obstacleGrid[0][i]:
                break
            mat[0][i] = 1

        for i in range(1, m):
            mat[i][0] = 0 if obstacleGrid[i][0] else mat[i - 1][0]
            for j in range(1, n):
                mat[i][j] = mat[i - 1][j] + mat[i][j - 1] if not obstacleGrid[i][j] else 0

        return mat[-1][-1]