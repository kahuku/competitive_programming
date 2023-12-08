from sys import stdin
from collections import defaultdict
import math

lines = [line.strip() for line in stdin.readlines()]

dirs = lines[0]

adj = defaultdict(list)
for i in range(2, len(lines)):
    line = lines[i]
    key = line[:3]
    a, b = line[7:10], line[12:15]
    adj[key].append(a)
    adj[key].append(b)

places = [k for k, v in adj.items() if k[2] == 'A']
out = []
for place in places:
    c = 0
    i = 0
    while True:
        if place[2] == 'Z':
            break

        if dirs[i] == 'L':
            place = adj[place][0]
        else:
            place = adj[place][1]

        c += 1
        i += 1
        i %= len(dirs)
    out.append(c)

print(math.lcm(*out))