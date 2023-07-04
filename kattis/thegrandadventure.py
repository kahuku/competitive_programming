adventures = []
for _ in range(int(input())):
    adventures.append(input())
for a in adventures:
    s = []
    possible = True
    for c in a:
        if c == '.': continue
        if c == '$' or c == '|' or c == '*': s.append(c)
        elif c == 't':
            if len(s) == 0 or s[-1] != '|':
                possible = False
                break
            s.pop()
        elif c == 'j':
            if len(s) == 0 or s[-1] != '*':
                possible = False
                break
            s.pop()
        elif c == 'b':
            if len(s) == 0 or s[-1] != '$':
                possible = False
                break
            s.pop()
    print('YES' if possible and len(s) == 0 else 'NO')
