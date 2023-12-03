from sys import stdin

grid = []
for line in stdin.readlines():
    grid.append(line.strip())

def is_valid(grid, x, y):
    return 0 <= x < len(grid) and 0 <= y < len(grid[x])

dirs = [(0, 1), (-1, 0), (1, 0), (0, -1), (1, 1), (-1, -1), (-1, 1), (1, -1)]

def look(grid, i, j, visited):
    print("LOOK")
    x, y = i, j
    while True:
        if is_valid(grid, x, y) and grid[x][y - 1].isdigit():
            y -= 1
        else:
            break
    
    print("start:", x, y, grid[x][y])
    num = ''
    while True:
        if is_valid(grid, x, y) and grid[x][y].isdigit():
            visited.add((x, y))
            num += grid[x][y]
            y += 1
        else:
            break
    
    print("-----")
    return int(num) if num else None

def search(grid, x, y):
    num1 = None
    num2 = None
    visited = set()
    for dir in dirs:
        dx, dy = dir
        if not is_valid(grid, x + dx, y + dy) or (x + dx, y + dy) in visited:
            continue
        c = grid[x + dx][y + dy]
        visited.add((x + dx, y + dy))
        if c.isdigit():
            print(x + dx, y + dy, c)
            if num1:
                num2 = look(grid, x + dx, y + dy, visited)
            else:
                num1 = look(grid, x + dx, y + dy, visited)

    print()
    return num1, num2

s = 0
for i in range(len(grid)):
    for j in range(len(grid[i])):
        if grid[i][j] == '*':
            num1, num2 = search(grid, i, j)
            # print(num1, num2)
            if num1 and num2:
                s += num1 * num2
        # break # UNCOMMENT

print(s)