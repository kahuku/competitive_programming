from collections import defaultdict
n = int(input())
j = 1
while n != 0:
    d = defaultdict(int)
    for i in range(n):
        d[input().split()[-1].lower()] += 1
    print(f"List {j}:")
    l = sorted(list(d.items()), key=lambda x: x[0])
    print("\n".join([f"{item[0]} | {item[1]}" for item in l]))
    n = int(input())
    j += 1