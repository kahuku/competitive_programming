def find_num(curr_num, grid):
    for x in range(3):
        for y in range(3):
            if (grid[y][x] == curr_num):
                return (y, x)

inp = []
inp1 = [int(i) for i in input().split(' ')]
inp.append(inp1)
inp2 = [int(i) for i in input().split(' ')]
inp.append(inp2)
inp3 = [int(i) for i in input().split(' ')]
inp.append(inp3)
#print(inp)

curr_num = 1
dist = 0

while curr_num < 9:
    start_loc = find_num(curr_num, inp)
    end_loc = find_num(curr_num + 1, inp)
    #sqrt((y2-y1)^2 + (x2-x1)^2)
    dist += ((end_loc[0] - start_loc[0]) ** 2 + (end_loc[1] - start_loc[1]) ** 2) ** 0.5
    curr_num += 1
print(dist)
