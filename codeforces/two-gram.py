from collections import defaultdict

_, s = input(), input()
d = defaultdict(int)
for i in range(len(s) - 1):
    twogram = s[i] + s[i + 1]
    d[twogram] += 1

print(max(d, key=d.get))
