r, c = map(int, input().split())
lot = [list(input()) for _ in range(r)]
counters = [0, 0, 0, 0, 0]
for i in range(r - 1):
    for j in range(c - 1):
        if lot[i][j] != '#' and lot[i][j+1] != '#' and lot[i+1][j] != '#' and lot[i+1][j+1] != '#':
            counters[(lot[i][j] == 'X') + (lot[i][j+1] == 'X') + (lot[i+1][j] == 'X') + (lot[i+1][j+1] == 'X')] += 1
for count in counters:
    print(count)