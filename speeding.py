n = int(input())

times = []
distances = []
for i in range(n):
    inp = [int(i) for i in input().split()]
    times.append(inp[0])
    distances.append(inp[1])

#print(times)
#print(distances)

j = 1
speeds = []
while j < len(distances):
    timeDiff = times[j] - times[j-1]
    milesDiff = distances[j] - distances[j-1]
    speeds.append(int(milesDiff / timeDiff))
    j += 1
speeds.sort()
print(speeds[len(speeds)-1])
