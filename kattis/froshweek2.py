n, m = map(int, input().split())
quiet = list(map(int, input().split()))
tasks = list(map(int, input().split()))
quiet.sort()
tasks.sort()
ans = 0
for j in range(min(n, m)):
    if tasks[j] >= quiet[ans]:
        ans += 1
print(ans)