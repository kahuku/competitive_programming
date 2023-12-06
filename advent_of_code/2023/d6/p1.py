from sys import stdin

lines = stdin.read().splitlines()
times = list(map(int, lines[0].split()[1:]))
dists = list(map(int, lines[1].split()[1:]))

p = 1
for t, d in zip(times, dists):
    c = 0
    for i in range(t + 1):
        if (t - i) * i > d:
            c += 1
    p *= c
print(p)