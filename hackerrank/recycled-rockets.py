m = float('inf')
for _ in range(int(input())):
    n, a = map(int, input().split())
    m = min(m, a // n)
print(m)