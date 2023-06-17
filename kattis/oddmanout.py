from collections import defaultdict
cases = int(input())
for i in range(cases):
    input()
    d = defaultdict(int)
    peeps = map(int, input().split())
    for person in peeps:
        d[person] += 1
    print(f"Case #{i + 1}: {sorted(d.items(), key=lambda x: x[1])[0][0]}")