n, a = map(int, input().split())
e = list(map(int, input().split()))
e.sort()
i = 0
while i < len(e):
    if e[i] + 1 > a: break
    a -= e[i] + 1
    i += 1
print(i)