import math
r, h, s = map(int, input().split())
while r != 0 or h != 0 or s != 0:
    angle = 360 - 2 * (math.acos(r / h) * (180 / math.pi))
    l = 2 * math.pi * r * (angle / 360)
    l += (((h ** 2 - r ** 2) ** 0.5) * 2)
    l *= ((100 + s) / 100)
    print(f"{l:.2f}")
    r, h, s = map(int, input().split())