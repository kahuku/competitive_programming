input()

log = [int(i) for i in input().split()]

s = 0.0
num = 0
for entry in log:
    if entry != -1:
        s += entry
        num += 1
p = s / num
print(p)
