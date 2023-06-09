x, y = list(map(int, input().split()))
if y == 1:
    if x == 0:
        print("ALL GOOD")
    else:
        print("IMPOSSIBLE")
else:
    print(x / (1 - y))