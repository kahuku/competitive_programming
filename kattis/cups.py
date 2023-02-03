n = int(input())
cups = []
for _ in range(n):
    s = input().split()
    if s[0][0] in ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']:
        cups.append((int(s[0]) / 2, s[1]))
    else:
        cups.append((int(s[1]), s[0]))
cups = sorted(cups, key=lambda x: x[0])
for cup in cups:
    print(cup[1])