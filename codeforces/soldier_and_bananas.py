l = [int(i) for i in input().split()]
banana_cost, cash, num_bananas = l[0], l[1], l[2]

for banana in range(1, num_bananas + 1):
    cash -= banana_cost * banana
    
if cash > 0:
    print(0)
else:
    print(cash * -1)