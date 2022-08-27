m = [int(i) for i in input().split()][0]
pixels = []
for i in range(m):
    row = input().split()
    for pixel in row:
        pixels.append(pixel)

if set(pixels).isdisjoint(['C', 'Y', 'M']):
    print("#Black&White")
else:
    print("#Color")
