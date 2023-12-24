# not finished
from sys import stdin
from collections import deque, defaultdict

def valid(x, y, dist, cost):
    return dist <= 3 and not d[(x, y, dist, cost)] and 0 <= x < len(grid) and 0 <= y < len(grid[0])

grid = [list(map(int, line.strip())) for line in stdin.readlines()]

m = float('inf')
q = deque()
q.append((0, 0, 0, 0))
d = defaultdict(bool)
d[(0, 0, 0, 0)] = True
while q:
    x, y, dist, cost = q.popleft()
    if not valid(x, y, dist, cost):
        continue
    cost += grid[x][y]
    if x == len(grid) - 1 and y == len(grid[0]) - 1:
        m = min(m, cost)
        continue
    for dx, dy in ((0, 1), (0, -1), (1, 0), (-1, 0)):
        nx, ny = x + dx, y + dy


print(m)