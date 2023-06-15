from collections import defaultdict
cards = input().split()
d = defaultdict(int)
for card in cards:
    d[card[0]] += 1
print(sorted(d.values(), reverse=True)[0])