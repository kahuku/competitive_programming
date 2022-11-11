import math


n = int(input())

l = []
for _ in range(n):
    l.append(int(input()))
    
min = math.inf
for i in range(len(l)):
    if l[i] + l[(i-2) % n] < min:
        min = l[i] + l[(i-2) % n]
print(min)