n = int(input())
l = sorted(list(map(int, input().split())))
s = 0
for i in range(len(l) - 1):
    s += ((l[i] - l[i + 1]) ** 2)
print(s)