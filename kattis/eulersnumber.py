n = int(input())
e = 0
fac = 1
for i in range(1, n + 2):
    e += 1 / (fac)
    fac *= i
print(e)