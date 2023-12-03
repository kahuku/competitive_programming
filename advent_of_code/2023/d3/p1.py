from sys import stdin

grid = []
for line in stdin.readlines():
    grid.append(line.strip())

def is_valid(grid, x, y):
    return 0 <= x < len(grid) and 0 <= y < len(grid[x])

dirs = [(0, 1), (1, 0), (0, -1), (-1, 0), (1, 1), (-1, -1), (-1, 1), (1, -1)]
def look(grid, x, y):
    for dir in dirs:
        dx, dy = dir
        if not is_valid(grid, x + dx, y + dy):
            continue
        c = grid[x + dx][y + dy]
        if not c.isdigit() and c != '.':
            return True
    return False

s = 0
for i in range(len(grid)):
    num = ''
    coords = []
    for j in range(len(grid[i])):
        if grid[i][j].isdigit():
            num += grid[i][j]
            coords.append((i, j))
        else:
            if num:
                add = False
                for coord in coords:
                    if look(grid, coord[0], coord[1]):
                        add = True
                        break
                if add:
                    # print(num)
                    s += int(num)
            num = ''
            coords = []
    if num:
        add = False
        for coord in coords:
            if look(grid, coord[0], coord[1]):
                add = True
                break
        if add:
            # print(num)
            s += int(num)
    num = ''
    coords = []

print(s)