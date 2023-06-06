from sys import stdin

def getScore(low, high):
    if high < low:
        low, high = high, low
    if low == 1 and high == 2:
        return 1000
    elif low == high:
        return 100 * low
    else:
        return 10 * high + low

for line in stdin.readlines():
    s0, s1, r0, r1 = list(map(int, line.split()))
    if s0 == s1 == r0 == r1 == 0:
        break
    score1 = getScore(s0, s1)
    score2 = getScore(r0, r1)
    if score1 > score2:
        print('Player 1 wins.')
    elif score1 < score2:
        print('Player 2 wins.')
    else:
        print('Tie.')