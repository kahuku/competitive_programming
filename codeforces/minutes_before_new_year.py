# 1283A

for _ in range(int(input())):
    h, m = map(int, input().split())
    m += (h * 60)
    print(24 * 60 - m)