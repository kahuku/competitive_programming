prev, s = None, ''
for char in input():
    if char != prev:
        s += char
    prev = char
print(s)