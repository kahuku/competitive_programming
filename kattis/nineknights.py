rows = []
for i in range(5):
    rows.append(list(input()))
knights = []
for i in range(5):
    for j in range(5):
        if rows[i][j] == 'k':
            knights.append((i, j))
if len(knights) != 9:
    print('invalid')
    exit()
for i in range(9):
    for j in range(i + 1, 9):
        a = abs(knights[i][0] - knights[j][0])
        b = abs(knights[i][1] - knights[j][1])
        if a + b == 3 and a != 0 and b != 0:
            print('invalid')
            exit()
print('valid')