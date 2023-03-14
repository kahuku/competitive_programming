class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        islands = 0

        def valid(x, y):
            return x >= 0 and x < len(grid) and y >= 0 and y < len(grid[0])

        def search(x, y):
            if not valid(x, y): return
            if grid[x][y] == '0': return
            grid[x][y] = '0'
            search(x + 1, y)
            search(x - 1, y)
            search(x, y + 1)
            search(x, y - 1)

        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] != '0':
                    islands += 1
                    search(i, j)

        return islands