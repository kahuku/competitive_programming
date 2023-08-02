n, k = map(int, input().split())
pokemon = []
selected = set()
for i in range(n):
    arr = [i]
    arr.extend([int(j) for j in input().split()])
    pokemon.append(arr)
for i in range(1, 4):
    pokemon.sort(key=lambda x: x[i], reverse=True)
    for j in range(k):
        selected.add(pokemon[j][0])
print(len(selected))