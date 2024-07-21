p, q = map(int, input().split())
d = {}
for _ in range(p):
    first, last = input().split()
    initials = first[0] + last[0]
    if initials not in d:
        d[initials] = first + ' ' + last
    else:
        d[initials] = 'ambiguous'
for _ in range(q):
    initials = input()
    if initials in d:
        print(d[initials])
    else:
        print('nobody')