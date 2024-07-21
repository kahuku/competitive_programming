n, k = map(int, input().split())
c = 0
for _ in range(n):
    c += k - len(set(list(input().split())))
print(c)