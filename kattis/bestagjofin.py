l = []
for _ in range(int(input())):
    name, fun = input().split()
    l.append((name, int(fun)))
print(sorted(l, key=lambda x: x[1], reverse=True)[0][0])