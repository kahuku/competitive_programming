num_cans, num_colors = [int(i) for i in input().split()]

cans = []
for i in range(num_cans):
    cans.append(int(input()))
cans.sort()

colors = []
for i in range(num_colors):
    colors.append(int(input()))

ans = 0
for color in colors:
    low = 0
    high = num_cans
    while low < high:
        mid = (low + high) // 2
        if cans[mid] < color:
            low = mid + 1
        else:
            high = mid
    ans += cans[high] - color

print(ans)
