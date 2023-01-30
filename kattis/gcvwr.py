g, t, _ = [int(i) for i in input().split()]
s = sum([int(i) for i in input().split()])
print(int((g - t) * .9 - s))