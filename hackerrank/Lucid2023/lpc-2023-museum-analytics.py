from collections import defaultdict
d = defaultdict(int)
for _ in range(int(input())):
    l = input().split(',')
    for i in l:
        d[i] += 1
top = sorted(d.items(), key=lambda x: x[1], reverse=True)[0]
print(top[0])
print(top[1])