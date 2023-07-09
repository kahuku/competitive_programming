n, _ = map(int, input().split())
l = list(map(int, input().split()))
filled = 0
skipped = 0
for i in range(len(l)):
    if l[i] + filled <= n:
        filled += l[i]
    else:
        skipped += 1
print(skipped)