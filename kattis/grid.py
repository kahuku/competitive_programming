from collections import deque

n, m = [int(i) for i in input().split()]
g = [list(map(int, input())) for _ in range(n)]
q = deque()
q.append((0, 0, 0))

def in_bounds(x, y):
    return 0 <= x < n and 0 <= y < m

v = set()
while q:
    x,y,d = q.popleft()
    if x == n - 1 and y == m - 1:
        print(d)
        quit()
    if (x, y) in v:
        continue
    v.add((x, y))
    for i, j in [[1, 0], [0, 1], [-1, 0], [0, -1]]:
        dist = g[x][y]
        a = x + i * dist
        b = y + j * dist
        if in_bounds(a, b):
            q.append((a, b, d+1))
print(-1)