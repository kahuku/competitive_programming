input(); l = list(map(int, input().split()))
s, m = 0, 0
for num in l:
    s += num
    m = max(m, num)
if s - m < m:
    print(m * 2)
else:
    print(s)