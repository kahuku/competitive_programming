from sys import stdin

def check(line):
    return sum([1 if i == 0 else 0 for i in line]) == len(line)

def next_line(line):
    nl = []
    for i in range(1, len(line)):
        nl.append(line[i] - line[i - 1])
    return nl

def conv(line):
    lines = [line]
    i = 0
    while not check(lines[i]):
        lines.append(next_line(lines[i]))
        i += 1
    lines[i].append(0)
    for j in range(i - 1, -1, -1):
        diff = lines[j + 1][-1]
        lines[j].append(lines[j][0] - diff)
    return lines[0][-1]

inp = stdin.read().splitlines()
inp = [list(map(int, line.split())) for line in inp]

c = 0
for line in inp:
    c += conv(line)
print(c)