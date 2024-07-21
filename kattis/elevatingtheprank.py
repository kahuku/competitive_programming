origin, destination = map(int, input().split())
nFloors = int(input())
floors = list(int(input()) for _ in range(nFloors))
if origin > destination:
    origin, destination = destination, origin
count = (destination - origin) * 4 + 10 * sum(1 for floor in floors if floor > origin and floor < destination)
print(count)