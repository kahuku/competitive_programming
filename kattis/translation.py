n = int(input())
s = input().split()
m = int(input())
d = {}
for _ in range(m):
    a, b = input().split()
    d[a] = b
o = []
for word in s:
    o.append(d[word])
print(' '.join(o))