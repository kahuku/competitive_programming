s = []
for char in input():
    if char == '<':
        s.pop()
    else:
        s.append(char)
print(''.join(s))