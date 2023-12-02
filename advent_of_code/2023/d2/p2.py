from sys import stdin
from collections import defaultdict

s = 0
for line in stdin.readlines():
    line = line.split(':')[1]
    games = line.split(';')

    d2 = defaultdict(int)
    for game in games:
        results = game.split(',')

        for result in results:
            n = int(result.split()[0])
            color = result.split()[1]
            d2[color] = max(d2[color], n)
    
    p = 1
    for _, v in d2.items():
        p *= v
    s += p

print(s)