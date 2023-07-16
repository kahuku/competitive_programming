n, m = map(int, input().split())
rankings = [f"T{i + 1}" for i in range(n)]
for _ in range(m):
    winner, loser = input().split()
    winner_index = rankings.index(winner)
    loser_index = rankings.index(loser)
    if winner_index > loser_index:
        rankings.pop(loser_index)
        rankings.insert(winner_index, loser)
print(' '.join(rankings)) 