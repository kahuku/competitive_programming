a, b, c, n = list(map(int, input().split()))
if a > 0 and b > 0 and c > 0 and n >= 3 and a + b + c >= n:
    print("YES")
else:
    print("NO")