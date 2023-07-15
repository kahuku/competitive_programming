_, p = map(int, input().split())
dists = sorted(list(map(int, input().split())))
dist = 0
for i in range(len(dists)):
    new_dist = p * (i + 1) - dists[i]
    dist = max(dist, new_dist)
print(dist + dists[0])