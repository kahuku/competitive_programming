for i in range(int(input())):
    snappers, snaps = map(int, input().split())
    works = True
    for j in range(snappers):
        if snaps % 2 == 0:
            works = False
        snaps //= 2

    print("Case #{}: {}".format(i + 1, "ON" if works else "OFF"))