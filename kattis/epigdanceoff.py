n, m, = map(int, input().split())
g = [input() for _ in range(n)]
c = 1
for i in range(m):
    if all(g[j][i] == '_' for j in range(n)):
        c += 1
print(c)