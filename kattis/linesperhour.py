import itertools
import operator

n, lph = map(int, input().split())
lines = sorted([int(input()) for _ in range(n)])
tot_lines = itertools.accumulate(lines, operator.add)
mid = next((i - 1 for i, x in enumerate(tot_lines, 1) if x > lph * 5), n)
if mid == -1:
    print(0)
else:
    print(mid)