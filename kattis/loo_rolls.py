l, n = [int(i) for i in input().split()]
rolls = 1
remaining = l % n
while remaining != 0:
    rolls += 1
    n -= remaining
    remaining = l % n
print(rolls)