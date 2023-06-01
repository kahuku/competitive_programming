n = [int(i) for i in input().split()][0]
x = [int(i) for i in input().split()]
s = 0
for i in range(len(x)):
    if s + x[i] <= n:
        s += x[i]
    else:
        break
print(len(x) - i)