n = int(input())
ways = [0, 1, 2, 4]
for i in range(4, n + 1):
    ways.append(ways[i-1] + ways[i-2] + ways[i-3])
print(ways[-1])