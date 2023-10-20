# this isn't working
def old():
    import sys
    sys.setrecursionlimit(10000000)

    w, h = map(int, input().split())
    g = [list(input()) for _ in range(h)]

    spos = (0, 0)
    for r in range(h):
        for c in range(w):
            if g[r][c] == 'P':
                spos = (r, c)
                break

    def valid(r, c):
        return r in range(0, h) and c in range(0, w) and g[r][c] != '#'

    def neig(r, c):
        s = (1, 0, -1, 0, 1)
        np = [(r + a, c + b) for a, b in zip(s, s[1:])] #s[:-1], s[1:]
        return [p for p in np if valid(*p)]

    visited = set()
    def flood(r, c, gl):
        if g[r][c] == 'G':
            gl += 1
        np = neig(r, c)
        if any(g[x][y] == 'T' for x, y in np):
            return gl
        for n in np:
            if n not in visited:
                visited.add(n)
                gl = flood(n[0], n[1], gl)
        return gl

    # visited.add(spos)
    print(flood(spos[0], spos[1], 0))


# revistited Oct 19, 2023
from collections import deque
w, h = map(int, input().split())
g = [input() for _ in range(h)]
q = deque()
for i in range(h):
    for j in range(w):
        if g[i][j]=="P":
            q.append((i, j))
v = set()
o = 0

dirs = [1, 0, -1, 0, 1]
def n(i, j):
    ne = []
    for k, l in zip(dirs, dirs[1:]):
        x, y = i + k, l + j
        if g[x][y] == 'T': return []
        elif g[x][y] != '#': ne.append((x, y))
    return ne

while q:
    i, j = q.popleft()
    if (i, j) in v:
        continue
    v.add((i, j))
    t = g[i][j]
    if t == 'G':
        o += 1
    for x, y in n(i, j):
        q.append((x, y))

print(o)