from collections import deque

def n(i, j):
    return [
        (i + 1, j + 1),
        (i + 1, j),
        (i + 1, j - 1),
        (i, j + 1),
        (i, j - 1),
        (i - 1, j + 1),
        (i - 1, j),
        (i - 1, j - 1)
    ]

def valid(x, y):
    return x >= 0 and x < len(grid) and y >= 0 and y < len(grid[0]) and grid[x][y] == '#'

def bfs(r, c):
    q = deque()
    q.append((r, c))
    while q:
        i, j = q.popleft()
        if visited[i][j]:
            continue
        visited[i][j] = True
        for x, y in n(i, j):
            if valid(x, y):
                q.append((x, y))

r, c = map(int, input().split())
grid = []
for _ in range(r):
    grid.append(list(input()))

visited = [[False for _ in range(c)] for _ in range(r)]

count = 0

for i in range(len(grid)):
    for j in range(len(grid[0])):
        if grid[i][j] == '#' and not visited[i][j]:
            count += 1
            bfs(i, j)

print(count)