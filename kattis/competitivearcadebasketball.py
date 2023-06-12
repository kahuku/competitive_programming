n, p, m = map(int, input().split())
players = {}
for _ in range(n): players[input()] = 0
winners = set()
for _ in range(m):
    name, score = input().split()
    players[name] += int(score)
    if players[name] >= p and name not in winners:
        print(name, 'wins!')
        winners.add(name)
if len(winners) == 0: print('No winner!')