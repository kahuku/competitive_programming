from collections import deque

def n(i, j):
    ne = []
    for k, l in zip(dirs, dirs[1:]):
       x, y = i + k, j + l
       if x >= len(grid) or x < 0 or y >= len(grid[0]) or y < 0 or grid[x][y] == 'W':
           continue
       ne.append((x, y))
    return ne 

def bfs(a, b):
    q = deque()
    q.append((a, b))
    while q:
        x, y = q.popleft()
        if visited[x][y]:
            continue
        visited[x][y] = True
        for i, j in n(x, y):
            q.append((i, j))

r, c = map(int, input().split())
grid = [list(input()) for _ in range(r)]
dirs = [1, 0, -1, 0, 1]

q = deque()
visited = [[False for _ in range(c)] for _ in range(r)]

# add starting land points to queue
for i in range(len(grid)):
    for j in range(len(grid[0])):
        if grid[i][j] == 'L':
            q.append((i, j))

count = 0
while q:
    x, y = q.popleft()
    if visited[x][y]:
        continue
    bfs(x, y)
    count += 1
print(count)