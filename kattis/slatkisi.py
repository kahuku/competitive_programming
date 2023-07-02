c, k = map(int, input().split())
k = 10 ** k
c /= k
c = round(c)
c *= k
print(c)