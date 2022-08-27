rooms, teams = int(input()), int(input())
out = []
[out.append(teams // rooms * "*") for _ in range(rooms)]
for i in range(teams % rooms):
    out[i] += "*"
[print(room) for room in out]