n, q = map(int, input().split())
locs = list(map(int, input().split()))
for _ in range(q):
    query = list(map(int, input().split()))
    if query[0] == 1:
        locs[query[1] - 1] = query[2]
    else:
        print(abs(locs[query[1] - 1] - locs[query[2] - 1]))