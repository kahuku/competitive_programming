x = int(input())
n = int(input())
p = []
for num in range(n):
    p.append(int(input()))

r = x
for i in range(n):
    r += (x - p[i])

print(r)
