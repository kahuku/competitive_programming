n = int(input())
while n != -1:
    adj = []
    for i in range(n):
        adj.append(list(map(int, input().split())))
    weak = []
    for i in range(n):
        for j in range(n):
            if adj[i][j] == 1:
                for k in range(n):
                    if adj[j][k] == 1 and adj[k][i] == 1:
                        weak.append(i)
                        break
    weak = list(set(weak))
    weak.sort()
    print(*[i for i in range(n) if i not in weak], sep=' ')
    n = int(input())