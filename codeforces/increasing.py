# 1742B
for _ in range(int(input())):
    n = int(input())
    x = set(map(int, input().split()))
    if len(x) == n:
        print("YES")
    else:
        print("NO")