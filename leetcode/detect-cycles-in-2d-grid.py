class Solution:
    def containsCycle(self, grid: List[List[str]]) -> bool:
        s1 = set()

        dirs = [1, 0, -1, 0, 1]
        def valid_neighbors(r, c, p):
            n = []
            for dx, dy in zip(dirs, dirs[1:]):
                nr, nc = r + dy, c + dx
                basic_checks = 0 <= nr < len(grid) and 0 <= nc < len(grid[0]) and grid[nr][nc] == grid[r][c]
                if basic_checks and (not p or not (nr == p[0] and nc == p[1])):
                    n.append((nr, nc))
            return n

        def dfs(r, c, p, s2):
            if (r, c) in s2:
                return True
            s2.add((r,c))
            s1.add((r, c))
            for nx, ny in valid_neighbors(r, c, p):
                if dfs(nx, ny, (r, c), s2):
                    return True
            return False

        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if (r, c) not in s1 and dfs(r, c, None, set()):
                    return True
        return False
    


class Solution:
    def containsCycle(self, grid: List[List[str]]) -> bool:
        s1 = set()

        dirs = [1, 0, -1, 0, 1]
        def valid_neighbors(r, c, p):
            n = []
            for dx, dy in zip(dirs, dirs[1:]):
                nr, nc = r + dy, c + dx
                if 0 <= nr < len(grid) and 0 <= nc < len(grid[0]) and grid[nr][nc] == grid[r][c] and (not p or not (nr == p[0] and nc == p[1])):
                    n.append((nr, nc))
            return n

        def dfs(r, c, p, s2):
            if (r, c) in s2:
                return True
            s2.add((r,c))
            s1.add((r, c))
            for nx, ny in valid_neighbors(r, c, p):
                if dfs(nx, ny, (r, c), s2):
                    return True
            return False

        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if (r, c) not in s1 and dfs(r, c, None, set()):
                    return True
        return False