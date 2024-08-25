r, c = map(int, input().split())
o = []
for row in range(r):
    l = input()
    for col, char in enumerate(l):
        if char == '*':
            o.append((row + 1, col + 1))
print(len(o))
for r, c in o:
    print(r, c)