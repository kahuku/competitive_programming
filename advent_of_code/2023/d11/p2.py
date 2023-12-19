from sys import stdin

EXP_DIST = 1000000

def print_grid(grid):
    for row in grid:
        print(row)

def parse_grid(grid):
    for i in range(len(grid)):
        if [grid[i][j][0] for j in range(len(grid[i]))].count('#') == 0:
            for j in range(len(grid[i])):
                grid[i][j] = ('.', True)

    for j in range(len(grid[0])):
        if [grid[i][j][0] for i in range(len(grid))].count('#') == 0:
            for i in range(len(grid)):
                grid[i][j] = ('.', True)

    points = []
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if grid[i][j][0] == '#':
                points.append((i, j))

    return points

def neighbors(grid, point):
    i, j = point
    dirs = [1, 0, -1, 0, 1]
    n = []
    for x, y in zip(dirs, dirs[1:]):
        nx, ny = i + x, j + y
        if 0 <= nx < len(grid) and 0 <= ny < len(grid[nx]):
            n.append((nx, ny))
    return n

def shortest_path(grid, start, end):
    visited = [[False for j in range(len(grid[i]))] for i in range(len(grid))]
    queue = [(start, 0)]
    visited[start[0]][start[1]] = True

    while len(queue) > 0:
        current, dist = queue.pop(0)
        if current == end:
            return dist
        for neighbor in neighbors(grid, current):
            if not visited[neighbor[0]][neighbor[1]]:
                new_dist = EXP_DIST if grid[neighbor[0]][neighbor[1]][1] else 1
                queue.append((neighbor, dist + new_dist))
                visited[neighbor[0]][neighbor[1]] = True

    return None

def main():
    grid = [list(line.strip()) for line in stdin.readlines()]
    grid = [[(grid[i][j], False) for j in range(len(grid[i]))] for i in range(len(grid))]
    points = parse_grid(grid)

    s = 0
    for i in range(len(points)):
        for j in range(i + 1, len(points)):
            s += shortest_path(grid, points[i], points[j])
    
    print(s)

if __name__ == '__main__':
    main()
