input(); rooms = input()
in_hand = 0
total = 0
for room in rooms:
    if room == '1':
        total += 1
        in_hand = 2
    else:
        if in_hand > 0:
            in_hand -= 1
            total += 1
print(total)