d = {}
for _ in range(int(input())):
    name, count = input().split()
    count = int(count)
    if name not in d:
        d[name] = count
    else:
        d[name] += count
print(sorted(d.items(), key=lambda x: x[1], reverse=True)[0][0])