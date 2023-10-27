r, c = map(int, input().split())
grid = [list(input()) for _ in range(r)]

out = [['.' for _ in range(c)] for _ in range(r)]
for co in range(c):
    apples = 0
    for ro in range(r):
        if grid[ro][co] == 'a':
            apples += 1
        elif grid[ro][co] == '#':
            out[ro][co] = '#'
            i = ro - 1
            while apples > 0:
                out[i][co] = 'a'
                i -= 1
                apples -= 1
    if apples > 0:
        i = ro
        while apples > 0:
            out[i][co] = 'a'
            i -= 1
            apples -= 1

print()
for row in out:
    print(''.join(row))