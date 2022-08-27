pattern = input()

cups = [1, 0, 0]

for letter in pattern:
    if letter == 'A':
        cups[0], cups[1] = cups[1], cups[0]
    elif letter == 'B':
        cups[1], cups[2] = cups[2], cups[1]
    elif letter == 'C':
        cups[0], cups[2] = cups[2], cups[0]

for i in range(3):
    if (cups[i] == 1):
        print(i + 1)
