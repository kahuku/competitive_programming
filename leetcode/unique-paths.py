class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        grid = [[-1] * n for _ in range(m)]
        grid[0][0] = 0
        if m == n == 1:
            return 1
        if m > 1:
            grid[1][0] = 1
        if n > 1:
            grid[0][1] = 1
        for row in range(m):
            for col in range(n):
                if grid[row][col] == -1:
                    if row > 0 and col > 0:
                        grid[row][col] = grid[row - 1][col] + grid[row][col - 1]
                    elif row == 0:
                        grid[row][col] = grid[row][col - 1]
                    elif col == 0:
                        grid[row][col] = grid[row - 1][col]
        return grid[-1][-1]