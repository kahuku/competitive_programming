n, cur, prev = map(int, input().split())
c = 0
for _ in range(n):
    num = int(input())
    if num > cur + prev:
        c += 1
        prev = cur
        cur = num
print(c)