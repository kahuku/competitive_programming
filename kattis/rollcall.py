from sys import stdin
from collections import defaultdict

names = [line.strip() for line in stdin.readlines()]
names.sort(key=lambda x: (x.split()[1], x.split()[0]))
d = defaultdict(int)
for name in names: d[name.split()[0]] += 1
for name in names:
    if d[name.split()[0]] > 1:
        print(name)
    else:
        print(name.split()[0])