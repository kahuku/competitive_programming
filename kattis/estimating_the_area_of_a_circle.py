import math
r, m, c = [float(i) for i in input().split()]
while r != m != c != 0:
    print(math.pi * r ** 2, 4 * r * r * c / m)
    r, m, c = [float(i) for i in input().split()]