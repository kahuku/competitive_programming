ranges = []
for _ in range(int(input())):
    ranges.append(list(map(int, input().split())))
high = 1000
low = 0
for r in ranges:
    low = max(low, r[0])
    high = min(high, r[1])
print("gunilla has a point" if low <= high else "edward is right")