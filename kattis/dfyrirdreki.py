a, b, c = [int(input()) for _ in range(3)]
d = b ** 2 - 4 * a * c
if d > 0:
    print(2)
elif d < 0:
    print(0)
else:
    print(1)