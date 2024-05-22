# 1619A
nl = int(input())
for _ in range(nl):
    line = input().strip()
    n = len(line)
    print("YES" if line[:n//2] == line[n//2:] else "NO")