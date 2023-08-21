days = int(input())
dists = []
out = []
for _ in range(3):
    dists.append(list(map(int, input().split())))
for day in range(days):
    out.append(str(sorted([dists[i][day] for i in range(3)])[1]))
print(' '.join(out))

# solution 2
days = int(input())
dists = [list(map(int, input().split())) for _ in range(3)]
print(' '.join([str(sorted([dists[i][day] for i in range(3)])[1]) for day in range(days)]))