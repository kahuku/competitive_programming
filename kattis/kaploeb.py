from collections import defaultdict
l, k, s = map(int, input().split())
d = defaultdict(int)
d2 = defaultdict(int)
for i in range(l):
    runner, time = input().split()
    m, s = time.split('.')
    runner = int(runner)
    d[runner] += int(m) * 60 + int(s)
    d2[runner] += 1
out = []
for key, v in d.items():
    if d2[key] == k:
        out.append((d[key], key))
out.sort()
for i in range(len(out)):
    print(out[i][1])