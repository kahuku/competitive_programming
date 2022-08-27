input()
cards = [int(i) for i in input().split()]
s, d = [0, 0]
for i in range(len(cards)):
    if i % 2 == 0:
        s += max(cards[0], cards[-1])
    else:
        d += max(cards[0], cards[-1])
    cards.remove(max(cards[0], cards[-1]))
print(s, d)