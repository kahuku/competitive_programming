inp = input().split()
h = int(inp[0])
num = 2 ** (h + 1)
directions = inp[1] if len(inp) == 2 else ''
sub = 1
directions = list(directions)
for i in range(len(directions)):
    if directions[i] == 'L':
        sub = sub * 2
    else:
        sub = sub * 2 + 1
print(num - sub)