_, cards= input(), [int(i) for i in input().split()]
cards.sort()

s = cards[0]
prev_num = cards[0]
for i in range(len(cards) - 1):
    curr_num = cards[i + 1]
    if curr_num != prev_num + 1:
        s += curr_num
    prev_num = curr_num

print(s)
