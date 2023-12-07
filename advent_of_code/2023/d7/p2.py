from sys import stdin
from collections import defaultdict, Counter

def jokerize(hand):
  target = (c:=Counter(hand)).most_common()[0][0]
  if target == "J" and hand != "JJJJJ":
    target = c.most_common()[1][0]
  return hand.replace("J", target)

def primary_sort(hand):
    hand = jokerize(hand)

    d = defaultdict(int)
    for card in hand:
        d[card] += 1
    items = sorted(d.items(), key=lambda x: x[1], reverse=True)

    if len(items) == 1:
        print(hand, 'five of a kind')
        return 0
    
    if len(items) == 2 and items[0][1] == 4:
        print(hand, 'four of a kind')
        return 1
    
    if len(items) == 2 and items[0][1] == 3 and items[1][1] == 2:
        print(hand, 'full house')
        return 2
    
    if len(items) == 3 and items[0][1] == 3 and items[1][1] == 1 and items[2][1] == 1:
        print(hand, 'three of a kind')
        return 3
    
    if len(items) == 3 and items[0][1] == 2 and items[1][1] == 2 and items[2][1] == 1:
        print(hand, 'two pair')
        return 4
    
    if len(items) == 4 and items[0][1] == 2 and items[1][1] == 1 and items[2][1] == 1 and items[3][1] == 1:
        print(hand, 'one pair')
        return 5

    print(hand, 'high card')
    return 6

def secondary_sort(hand):
    rankings = ['A', 'K', 'Q', 'T', '9', '8', '7', '6', '5', '4', '3', '2', 'J']
    return [rankings.index(card) for card in hand]

inp = stdin.read().split('\n')
inp = [line.split() for line in inp]

bets = sorted(inp, key=lambda x: (primary_sort(x[0]), secondary_sort(x[0])), reverse=True)

c = 0
for i in range(len(bets)):
    # print(bets[i])
    c += (i + 1) * int(bets[i][1])
print(c)