from queue import *
class Solution:
    def shortestBridge(self, grid: List[List[int]]) -> int:        
        def findIsland(grid):
            def dfs(r, c, grid, island):
                if r < 0 or r >= len(grid) or c < 0 or c >= len(grid[0]) or (r, c) in visited or grid[r][c] != 1:
                    return island
                island.append((r, c))
                visited.add((r, c))
                island = dfs(r - 1, c, grid, island)
                island = dfs(r + 1, c, grid, island)
                island = dfs(r, c + 1, grid, island)
                island = dfs(r, c - 1, grid, island)
                return island

            visited = set()

            for r in range(len(grid)):
                for c in range(len(grid[r])):
                    if grid[r][c] == 1:
                        return dfs(r, c, grid, [])

        q = Queue()
        i = 0
        first_island = findIsland(grid)
        island_set = set(first_island)
        print("island", first_island)
        q.put(first_island)
        print("q", q)
        visited2 = set()
        while not q.empty():
            i += 1
            curr_iteration = q.get()
            next_iteration = []
            print("curr", curr_iteration)
            while len(curr_iteration):
                r, c = curr_iteration.pop()
                if (r, c) in visited2 or r < 0 or r >= len(grid) or c < 0 or c >= len(grid[0]):
                    continue
                visited2.add((r, c))
                if grid[r][c] == 1 and (r, c) not in island_set:
                    print("coords", r, c)
                    return i - 2
                next_iteration.append((r + 1, c))
                next_iteration.append((r - 1, c))
                next_iteration.append((r, c + 1))
                next_iteration.append((r, c - 1))
            q.put(next_iteration)
        return -1