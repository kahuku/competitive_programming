for _ in range(int(input())):
    nPrizes, nStickers = map(int, input().split())
    prizes = []
    for _ in range(nPrizes):
        inp = list(map(int, input().split()))
        prizes.append((inp[1:-1], inp[-1]))
    stickers = [0] + list(map(int, input().split()))
    cash = 0
    for prize in prizes:
        mi = float('inf')
        for sticker in prize[0]:
            mi = min(mi, stickers[sticker])
        cash += max(0, prize[1] * mi)
    print(cash)