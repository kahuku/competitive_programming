def bottom_up(items, maxWeight):
    dp = [[0] * (maxWeight + 1) for _ in range(len(items) + 1)] # dp[i][w]
    for i in range(1, len(items) + 1):
        itemVal, itemWeight = items[i - 1]
        for allowedWeight in range(maxWeight + 1):
            if itemWeight <= allowedWeight:
                dontTake = dp[i - 1][allowedWeight]
                take = dp[i - 1][allowedWeight - itemWeight] + itemVal
            
                if dontTake > take:
                    dp[i][allowedWeight] = dontTake
                else:
                    dp[i][allowedWeight] = take
            else:
                dp[i][allowedWeight] = dp[i - 1][allowedWeight]

    w = maxWeight
    indexes = []
    for i in range(len(items), 0, -1):
        if dp[i][w] != dp[i - 1][w]:
            indexes.append(i - 1)
            w -= items[i - 1][1]

    return indexes

#input parsing

from sys import stdin
lines = stdin.readlines()
cases = []
counter = -1
count = -2
currCase = []
for i, line in enumerate(lines):
    line = list(map(int, line.split()))

    if counter == -1:
        count = line[1] + 1
        counter = 0

    currCase.append(line)
    counter += 1

    if counter == count:
        cases.append(currCase)
        currCase = []
        counter = -1
        count = -2

# actual problem

for case in cases:
    maxWeight, nItems = case[0]
    items = case[1:] # [value, weight]
    indexes = bottom_up(items, maxWeight)
    print(len(indexes))
    print(' '.join(map(str, indexes)))