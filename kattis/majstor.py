from collections import defaultdict

rounds, moves, n_friends, f_moves = int(input()), input(), int(input()), []
for i in range(n_friends):
    f_moves.append(input())

score = 0
for i in range(rounds):
    move = moves[i]
    
    for friend in f_moves:
        f_move = friend[i]
        if f_move == move:
            score += 1
        elif f_move == 'S' and move == 'R' or f_move == 'R' and move == 'P' or f_move == 'P' and move == 'S':
            score += 2

print(score)

score = 0
for i in range(rounds):
    d = defaultdict(int)
    round_moves = [j[i] for j in f_moves]
    for m in round_moves:
        d[m] += 1
    
    s_score = 2 * d['P'] + d['S']
    p_score = 2 * d['R'] + d['P']
    r_score = 2 * d['S'] + d['R']
    score += max(s_score, p_score, r_score)
print(score)