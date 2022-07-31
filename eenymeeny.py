rot_len = len(input().split())
kids = [input() for _ in range(int(input()))]
a, b, index, team1 = [], [], 0, True
while len(kids) > 0:
    index = (index + rot_len - 1) % len(kids)
    if team1:
        a.append(kids.pop(index))
    else:
        b.append(kids.pop(index))
    team1 = not team1

for l in [a, b]:
    print(len(l))
    [print(element) for element in l]