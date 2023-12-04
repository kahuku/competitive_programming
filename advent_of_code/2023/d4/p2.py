from sys import stdin
from collections import defaultdict

d = defaultdict(int)
s = 0
for line in stdin.readlines():
    num = int(line.split()[1][:-1])
    winning, have = line.split(':')[1].split('|')
    winning = winning.split()
    have = have.split()

    d[num] += 1
    s += d[num]

    se = set()
    for w in winning:
        se.add(w)

    c = 0
    for h in have:
        if h in se:
            c += 1

    for i in range(num + 1, num + c + 1):
        # d[i] += 1
        d[i] += d[num]

print(s)
print(d)