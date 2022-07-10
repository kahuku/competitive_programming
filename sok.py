a, b, c = [float(i) for i in input().split()]
x, y, z = [int(i) for i in input().split()]
q = min(a/x, b/y, c/z)
print(a - x * q, b - y * q, c - z * q)
