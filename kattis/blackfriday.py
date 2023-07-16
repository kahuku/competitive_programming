# does not work
n = int(input())
rolls = [int(x) for x in input().split()]
counts = {throw: rolls.count(throw) for throw in rolls}
possible = {}
for k, v in enumerate(rolls):
    if counts[v] == 1 and v not in possible:
        possible[k + 1] = v
if len(possible) == 0:
    print("none")
else:
    print(max(possible, key=lambda x: possible[x]))