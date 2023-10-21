m, s = int(input()), int(input())
stocks = []
for _ in range(s):
    input()
    stocks.append([int(x) for x in input().split()])
max_val = 0
min_val = 0
for i in range(m):
    inc = float('-inf')
    dec = float('inf')
    for j in range(s):
        change = (5000 // stocks[j][i]) * (stocks[j][-1] - stocks[j][i])
        inc = max(inc, change)
        dec = min(dec, change)
    if inc > 0:
        max_val += inc
    if dec < 0:
        min_val += dec
print(f"Max: {max_val}")
print(f"Min: {min_val}")