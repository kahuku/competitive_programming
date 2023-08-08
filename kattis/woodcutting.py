n = int(input())
for _ in range(n):
    m = int(input())
    times = []
    for _ in range(m):
        times.append(sum(list(map(int, input().split()))[1:]))
    times.sort()
    total = times[0]
    for i in range(1, m):
        times[i] += times[i-1]
        total += times[i]
    print(total/m)
