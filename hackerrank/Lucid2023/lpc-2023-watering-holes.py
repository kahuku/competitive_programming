from collections import defaultdict
d = defaultdict(set)
d2 = defaultdict(int)
found = set()
for _ in range(int(input())):
    dino, hole = input().split()
    if dino in found:
        curr_hole = d2[dino]
        d[curr_hole].remove(dino)
    found.add(dino)
    d[hole].add(dino)
    d2[dino] = hole
s = sorted(d.items(), key=lambda x: int(x[0]))
for i in range(len(s)):
    if s[i][0] == '0':
        continue
    dinos = sorted(list(s[i][1]))
    if len(dinos) == 0:
        print(s[i][0], 'n/a')
    else:
        print(s[i][0], ' '.join(dinos))