n = int(input())
s = set()
out = []
for _ in range(n):
    a, b = input().split()
    if a not in s:
        s.add(a)
        out.append(a + ' ' + b)
    if len(s) == 12:
        break

for line in out:
    print(line)