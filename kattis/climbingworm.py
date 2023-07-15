a, b, h = map(int, input().split())
height = 0
count = 0
while height < h:
    height += a
    count += 1
    if height >= h:
        break
    height -= b
print(count)