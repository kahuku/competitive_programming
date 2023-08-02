def dist(a, b):
    return abs(a[0] - b[0]) + abs(a[1] - b[1])

n = int(input())
grid = []
for i in range(n):
    grid.append(list(input()))

houses = []
spies = []
for i in range(n):
    for j in range(n):
        if grid[i][j] == 'H':
            houses.append((i, j))
        elif grid[i][j] == 'S':
            spies.append((i, j))

ans = 0
for spy in spies:
    min_dist = float('inf')
    for house in houses:
        min_dist = min(min_dist, dist(spy, house))
    ans = max(ans, min_dist)
print(ans)