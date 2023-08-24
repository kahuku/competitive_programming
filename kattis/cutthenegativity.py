from collections import defaultdict
lines = []
d = defaultdict(list)
for _ in range(int(input())):
    lines.append(list(map(int, input().split())))
for i in range(len(lines)):
    for j in range(len(lines[i])):
        cost = lines[i][j]
        if cost != -1:
            d[i + 1].append((j + 1, cost))
print(sum([len(v) for v in d.values()]))
for k, v in d.items():
    for dest, cost in v:
        print(k, dest, cost)