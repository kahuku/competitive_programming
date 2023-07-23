def get_distance(x1, y1, x2, y2):
    return ((x1 - x2) ** 2 + (y1 - y2) ** 2) ** 0.5

from sys import stdin
lines = stdin.readlines()
g_x, g_y, d_x, d_y = map(float, lines[0].split())
coordinates = [map(float, line.split()) for line in lines[1:]]
for x, y in coordinates:
    if get_distance(x, y, g_x, g_y) * 2 <= get_distance(x, y, d_x, d_y):
        print(f"The gopher can escape through the hole at ({x:.3f},{y:.3f}).")
        exit(0)
print("The gopher cannot escape.")