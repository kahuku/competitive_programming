class Solution:
    def countPaths(self, grid):
        rows = len(grid)
        cols = len(grid[0])
        mod = 10 ** 9 + 7

        @lru_cache(None)
        def valid(x, y):
            return 0 <= x < rows and 0 <= y < cols

        dirs = [1, 0, -1, 0, 1]
        @lru_cache(None)
        def neighbors(x, y):
            n = []
            for i, j in zip(dirs, dirs[1:]):
                if valid(x + i, y + j):
                    n.append((x + i, y + j))
            return n

        @lru_cache(None)
        def count(row, col):
            res = 1
            for x, y in neighbors(row, col):
                if grid[x][y] > grid[row][col]:
                    res += count(x, y)
            return res % mod

        out = 0
        for i in range(rows):
            for j in range(cols):
                out += (count(i, j) % mod)
        return out % mod