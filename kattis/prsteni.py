import math
_, radii = input(), [int(i) for i in input().split()]
for radius in radii[1:]:
    g = math.gcd(radii[0], radius)
    num, den = radii[0] // g, radius // g
    print(str(num) + '/' + str(den))