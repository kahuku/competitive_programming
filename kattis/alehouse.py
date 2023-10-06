n, k = map(int, input().split())
changes = []
for _ in range(n):
    a, b = map(int, input().split())
    changes.append((a, 1))
    changes.append((b + k, -1)) # because I will NOT see them if I enter more than k seconds after b
changes.sort(key=lambda x: (x[0], -x[1])) # count those entering for the current time before I count those leaving at the current time
best = overlap = 0
for _, i in changes:
    overlap += i
    best = max(best, overlap)
print(best)