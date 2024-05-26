# 1878A
for _ in range(int(input())):
    n, k = map(int, input().split())
    print("YES" if k in list(map(int, input().split())) else "NO")