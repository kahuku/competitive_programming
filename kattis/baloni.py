from collections import defaultdict

_, balloons = input(), [int(i) for i in input().split()]
darts = 0
d = defaultdict(int)
for balloon in balloons:
    if d[balloon + 1] > 0:
        d[balloon + 1] -= 1
    else:
        darts += 1
    d[balloon] += 1

print(darts)