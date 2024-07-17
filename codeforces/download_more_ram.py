# 1629A

for _ in range(int(input())):
    n, k = map(int, input().split())
    costs, upgrades = map(int, input().split()), map(int, input().split())
    zipped = zip(costs, upgrades)
    sZipped = sorted(zipped, key=lambda x: x[0])
    for cost, upgrade in sZipped:
        if cost <= k:
            k += upgrade
    print(k)