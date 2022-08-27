def dist(a, b): return ((b[1] - a[1]) ** 2 + (a[0] - b[0]) ** 2 ) ** 0.5
data = [int(i) for i in input().split()]
a_start, b_start, a_end, b_end = [data[0], data[1]], [data[2], data[3]], [data[4], data[5]], [data[6], data[7]]
print(max(dist(a_start, b_start), dist(a_end, b_end)))