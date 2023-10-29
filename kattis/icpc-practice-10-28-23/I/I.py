# code credit: Kim KangJin
# unfinished

import math
from sys import stdin

PI = math.pi

raw = stdin.readlines()
n, r, s, w, f, l1, l2 = map(float, raw[0].split())
lengths = [float(i) for i in raw[1:]]

out = []
for race_len in lengths:
    # r1
    x = 0
    y = 0
    r1 = r + l1
    degree = ( ((race_len - s) * 360) / (2 * PI * r1) ) % 360
    print(degree)

    if degree > 180:
        degree = degree - 180
        rad_deg = math.radians(degree)

        a = r1 / math.cos(rad_deg)
        w = math.sqrt(a ** 2 - r1 ** 2)
        x = 0 - (s-f) + w
        y = 0 + r1
    elif degree < 180:
        degree = degree - 90
        rad_deg = math.radians(degree)

        h = r1 * math.sin(rad_deg)
        w = math.sqrt(r1 ** 2 - h ** 2)

        x = 0 - (s-f) - w
        y = 0 + h
    elif degree == 180:
        x = 0 - (s-f)
        y = 0 + r1
    
    out.append((x,y))

for line in out:
    print(out)

'''
print("h")
    print(h)
    print("w")
    print(w)

     if origDegree > 180:
        l1x = 0 - (s-f) + w
        l1y = 0 + r1
        out.append((l1x, l1y))
    else:
        l1x = 0 - (s-f) - w
        l1y = 0 + h
        out.append((l1x, l1y))
    break
'''