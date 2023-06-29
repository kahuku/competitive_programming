n, k = map(int, input().split())
colors = list(map(int, input().split()))
d = {}
for i in range(k):
    d[i+1] = 0
for i in range(n):
    d[colors[i]] += 1
mi = min(d.values())
l = sorted(list(d.items()), key=lambda x: x[1])
li = [x[0] for x in l if x[1] == mi]
print(len(li))
print(' '.join(map(str, li)))