n, s = map(int, input().split())
for _ in range(n):
    l, h = map(int, input().split())
    if l <= s <= h:
        s += 1
print(s)