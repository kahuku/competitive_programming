import string

rows, cols, classes = [int(i) for i in input().split()]

group = [[char for char in input()] for i in range(rows)]

class_color = dict.fromkeys(string.ascii_uppercase, 0)
count = 0

for i in range(cols):
    col = set([group[j][i] for j in range(rows)])

    determined = False
    for student in col:
        if class_color[student] != 0:
            determined = True
            break

    if not determined:
        for student in col:
            class_color[student] += 1
        count += 1
    else:
        for student in col:
            class_color[student] += 1

print(count)
