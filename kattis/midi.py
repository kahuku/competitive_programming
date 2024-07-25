a = []
for _ in range(int(input())):
    a.append(input()[::-1])
print(*a[::-1], sep='')