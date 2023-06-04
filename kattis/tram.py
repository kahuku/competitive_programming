n = int(input())
s = 0
for _ in range(n):
    x, y = map(int, input().split())
    s += y-x
print('%.3f' % (s/n))