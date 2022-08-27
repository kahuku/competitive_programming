_, game_record = input(), input()
wins = {'D': 0, 'A': 0}
for winner in game_record:
    wins[winner] += 1
if wins['D'] > wins['A']:
    print("Danik")
elif wins['D'] < wins['A']:
    print("Anton")
else:
    print("Friendship")
