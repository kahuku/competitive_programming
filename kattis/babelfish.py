from sys import stdin
lines = [line.strip() for line in stdin.readlines()]
d = {}
for i, line in enumerate(lines):
    if line == '':
        break
    a, b = line.split()
    d[b] = a
for j in range(i + 1, len(lines)):
    word = lines[j]
    if word in d:
        print(d[word])
    else:
        print("eh")