from collections import defaultdict

dice = [int(i) for i in input().split()]
die1, die2 = dice[0], dice[1]

d = defaultdict(int)
for i in range(1, die1 + 1):
    for j in range(1, die2 + 1):
        d[i + j] += 1

[print(k) for k, v in d.items() if v == max(d.values())]