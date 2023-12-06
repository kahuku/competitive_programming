from sys import stdin

lines = stdin.read().splitlines()
time = int(''.join(lines[0].split()[1:]))
dist = int(''.join(lines[1].split()[1:]))

c = 0
for i in range(time + 1):
    if (time - i) * i > dist:
        c += 1
print(c)