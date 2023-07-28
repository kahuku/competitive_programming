from sys import stdin

d = {
    'B': 1, 'F': 1, 'P': 1, 'V': 1,
    'C': 2, 'G': 2, 'J': 2, 'K': 2, 'Q': 2, 'S': 2, 'X': 2, 'Z': 2,
    'D': 3, 'T': 3,
    'L': 4,
    'M': 5, 'N': 5,
    'R': 6,
    '@': 7
}

for line in stdin.readlines():
    line = line.strip()
    prev = '@'
    s = ''
    for c in line:
        if c in d.keys() and d[c] != d[prev]:
            s += str(d[c])
            prev = c
        elif c not in d.keys():
            prev = '@'
    print(s)