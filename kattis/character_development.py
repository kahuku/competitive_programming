from math import comb
n = int(input())
sum = 0
for i in range(2, n+1):
    sum += comb(n, i)

print(sum)