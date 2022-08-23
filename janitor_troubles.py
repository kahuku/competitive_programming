a, b, c, d = [int(i) for i in input().split()]
semiperimeter = (a + b + c + d) / 2
print(((semiperimeter - a) * (semiperimeter - b) * (semiperimeter - c) * (semiperimeter - d)) ** 0.5)