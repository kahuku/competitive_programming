from sys import stdin

s = 0
for line in stdin.readlines():
    winning, have = line.split(':')[1].split('|')
    winning = winning.split()
    have = have.split()

    se = set()
    for w in winning:
        se.add(w)

    c = 0
    for h in have:
        if h in se:
            c += 1
    
    if c != 0:
        s += 2 ** (c - 1)

print(s)