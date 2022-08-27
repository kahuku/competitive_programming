cases = int(input())
for i in range(cases):
    distances = [int(i) for i in input().split()]
    timur = distances[0]
    distances.sort(reverse=True)
    print(distances.index(timur))