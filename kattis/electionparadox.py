n, l = int(input()), list(map(int, input().split()))
c = 0
l = sorted(l, reverse=True)
i = n // 2
c += sum(l[:i])
for j in range(i, len(l)):
    c += l[j] // 2
print(c)