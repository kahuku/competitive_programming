r, b = map(int, input().split())
w = int(((r / 2) + 2 + ((((r / 2) + 2) ** 2) - 4 *(r + b)) ** 0.5) / 2)
l = int((r + b) / w)
print(max(l, w), min(l, w))