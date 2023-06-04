input(); dists = list(map(int, input().split()))
s = sum(dists)
t = {s-i for i in dists}
print(len(t))
print(*sorted(t))