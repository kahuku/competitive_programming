d_vals, vals = {'A': 11, 'K': 4, 'Q': 3, 'J': 20, 'T': 10, '9': 14, '8': 0, '7': 0}, {'A': 11, 'K': 4, 'Q': 3, 'J': 2, 'T': 10, '9': 0, '8': 0, '7': 0}
x = input().split()
hands, d_suit = int(x[0]), x[1]
s = 0
for _ in range(4 * hands):
    card = input()
    if card[1] == d_suit:
        s += d_vals[card[0]]
    else:
        s += vals[card[0]]
print(s)