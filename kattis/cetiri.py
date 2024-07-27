a, b, c = sorted(list(map(int, input().split())))
if c - b > b - a:
    print(b + b - a)
elif c - b < b - a:
    print(a + c - b)
else:
    print(c + c - b)