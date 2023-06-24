for i in range(int(input())):
    s = input()
    n = len(s)
    m = 1
    while m * m < n:
        m += 1
    s += '*' * (m * m - n)
    square = [s[i:i+m] for i in range(0, m * m, m)]
    new_square = [[] for _ in range(m)]
    for i in range(m):
        for j in range(m):
            new_square[j].append(square[i][j])
    s = ''
    for line in new_square:
        s += ''.join(line[::-1]).replace('*', '')
    print(s)