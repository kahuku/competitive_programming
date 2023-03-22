# TLE

from collections import deque

class Solution:
    def shortestPath(self, grid: List[List[int]], k: int) -> int:
        def valid(r, c):
            return r >= 0 and r < len(grid) and c >= 0 and c < len(grid[0])

        q = deque()
        q.append((0, 0, k))
        ans = 0
        while q:
            q_len = len(q)
            for i in range(q_len):
                row, col, breaks = q.popleft()

                # base case - we have reached the end
                if row == len(grid) - 1 and col == len(grid[0]) - 1:
                    return ans

                # if we are on a block, decrement our lives
                if grid[row][col]:
                    breaks -= 1
                
                # if we removed too many obstacles
                if breaks < 0:
                    continue

                # search neighboring cells if in bounds
                if valid(row + 1, col):
                    q.append((row + 1, col, breaks))
                if valid(row - 1, col):
                    q.append((row - 1, col, breaks))
                if valid(row, col + 1):
                    q.append((row, col + 1, breaks))
                if valid(row, col - 1):
                    q.append((row, col - 1, breaks))
                
            # we've searched every square ans steps away
            ans += 1

        # no solutions
        return -1
    
# okay so this one works but I tried the above with a set and it still TLEs, but for some reason this works   
from collections import deque

class Solution:
    def shortestPath(self, grid: List[List[int]], k: int) -> int:
        def valid(r, c):
            return r >= 0 and r < len(grid) and c >= 0 and c < len(grid[0])

        q = deque()
        q.append((0, 0, k))
        ans = 0
        s = set()
        while q:
            q_len = len(q)
            for i in range(q_len):
                row, col, breaks = q.popleft()

                if (row, col, breaks) in s:
                    continue
                s.add((row, col, breaks))

                if row < 0 or col < 0 or row == len(grid) or col == len(grid[0]):
                    continue

                # base case - we have reached the end
                if row == len(grid) - 1 and col == len(grid[0]) - 1:
                    return ans

                # if we are on a block, decrement our lives
                if grid[row][col]:
                    breaks -= 1
                
                # if we removed too many obstacles
                if breaks < 0:
                    continue

                # search neighboring cells if in bounds and not visited
                q.append((row + 1, col, breaks))
                q.append((row - 1, col, breaks))
                q.append((row, col + 1, breaks))
                q.append((row, col - 1, breaks))
                
            # we've searched every square ans steps away
            ans += 1

        # no solutions
        return -1