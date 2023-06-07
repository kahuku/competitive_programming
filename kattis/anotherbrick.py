h, w, _ = list(map(int, input().split()))
bricks = list(map(int, input().split()))
i = 0
w2 = w
while i < len(bricks):
    if bricks[i] > w2:
        print("NO")
        exit()
    w2 -= bricks[i]
    if w2 == 0:
        w2 = w
        h -= 1
    if h == 0:
        break
    i += 1
print("YES" if h == 0 else "NO")