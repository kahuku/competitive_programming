items, prices = int(input()), sorted([int(i) for i in input().split()], reverse=True)
print(0 if len(prices) < 3 else sum(prices[2::3]))