n = int(input())
prev = [float(x) for x in input().split()]
total = 0
for i in range(n - 1):
    curr = [float(x) for x in input().split()]
    total += (curr[0] - prev[0]) * (curr[1] + prev[1]) / 2
    prev = curr
print(total / 1000)