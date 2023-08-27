for _ in range(int(input())):
    turtles = list(map(int, input().split()))
    total = 0
    for i in range(1, len(turtles)):
        if turtles[i] > 2 * turtles[i - 1]:
            total += turtles[i] - 2 * turtles[i - 1]
    print(total)