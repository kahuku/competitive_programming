d = {
    '.': 20,
    'O': 10,
    '\\': 25,
    '/': 25,
    'A': 35,
    '^': 5,
    'v': 22
}
s = 0
for _ in range(int(input().split()[0])):
    for char in input():
        s += d[char]
print(s)