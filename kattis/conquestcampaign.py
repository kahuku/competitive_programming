from collections import deque

dirs = [1, 0, -1, 0, 1]
def ne(i, j):
    n = []
    for r, c in zip(dirs, dirs[1:]):
        x, y = i + r, j + c
        if valid(x, y):
            n.append((x, y))
    return n

def valid(x, y):
    return 0 <= x < len(visited) and 0 <= y < len(visited[0])

r, c, n = map(int, input().split())
visited = [[False for _ in range(c)] for _ in range(r)]
q = deque()
for _ in range(n):
    a, b = map(int, input().split())
    if (a - 1, b - 1) not in q:
        q.append((a - 1, b - 1, 0))
    
m = 0
while q:
    x, y, day = q.popleft()
    m = max(m, day)
    if visited[x][y]:
        continue
    visited[x][y] = True
    for i, j in ne(x, y):
        q.append((i, j, day + 1))

print(m)