a, b = int(input()), int(input())
c = (b - a + 720) % 360 # rotate right
d = -1 * ((a - b + 720) % 360) # rotate left
if abs(c) == 180:
    print(180)
elif abs(c) < abs(d):
    print(c)
else:
    print(d)