for _ in range(int(input())):
    direction, change, hours, minutes = input().split()
    change, hours, minutes = int(change), int(hours), int(minutes)
    if direction == 'B':
        change = -change
    minutes += change
    hours += minutes // 60
    minutes %= 60
    hours %= 24
    print(hours, minutes)