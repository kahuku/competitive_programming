input()
log = [int(i) for i in input().split()]

s = 0
for num in log:
    if num < 0:
        s += 1
print(s)
