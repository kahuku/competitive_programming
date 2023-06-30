from collections import defaultdict
n = int(input())
while n != 0:
    d = defaultdict(list)
    for _ in range(n):
        l = input().split()
        name, items = l[0], l[1:]
        for item in items:
            d[item].append(name)
    for item in sorted(d):
        print(item, " ".join(sorted(d[item])))
    print()
    n = int(input())