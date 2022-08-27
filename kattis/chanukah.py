cases = int(input())
for i, case in enumerate(range(cases)):
    days = [int(i) for i in input().split()][1]
    candles = days
    for day in range(1, days + 1):
        candles += day
    print(i + 1, candles)