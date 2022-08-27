n = int(input())
qaly = 0
for _ in range(n):
    inp = [float(i) for i in input().split()]
    qaly += inp[0] * inp[1]
print(qaly)