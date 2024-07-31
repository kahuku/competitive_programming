c1, y = 0, 0
for c in input():
    if c == 'a' or c == 'e' or c == 'i' or c == 'o' or c == 'u':
        c1 += 1
    if c == 'y':
        y += 1
print(c1, c1 + y)