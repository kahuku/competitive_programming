def lowPressureSystem(grid, r, c):
    cell = grid[r][c]
    return cell < grid[r-1][c] and cell < grid[r+1][c] and cell < grid[r][c-1] and cell < grid[r][c+1]

nr, nc = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(nr)]
for r in range(1, nr - 1):
    for c in range(1, nc - 1):
        if lowPressureSystem(grid, r, c):
            print('Jebb')
            exit(0)
print("Neibb")