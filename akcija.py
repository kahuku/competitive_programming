n = int(input())

prices = []
for price in range(n):
    prices.append(int(input()))

prices.sort(reverse=True)
i = 0
total = 0
#print(prices)
while i < len(prices):
    #print("{} % 3 = {}".format(i, i % 3))
    if ((i + 1) % 3 != 0 or i == 0):
        #print("Price: " + str(prices[i]))
        total += prices[i]
    i += 1
print(total)
