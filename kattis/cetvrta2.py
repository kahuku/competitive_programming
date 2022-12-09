from collections import defaultdict
di = defaultdict(int)
dj = defaultdict(int)
for _ in range(3):
    a, b = [int(i) for i in input().split()]
    di[a] += 1
    dj[b] += 1

c = list(dict(sorted(di.items(), key=lambda item: item[1])).keys())[0]
d = list(dict(sorted(dj.items(), key=lambda item: item[1])).keys())[0]
print(c, d)