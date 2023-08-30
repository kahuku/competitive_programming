n, m = map(int, input().split())
ladder = list(range(1, n+1))
for _ in range(m):
    i = int(input())
    ladder[i-1], ladder[i] = ladder[i], ladder[i-1]
print('\n'.join(map(str, ladder)))