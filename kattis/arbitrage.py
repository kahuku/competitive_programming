def arbitrate(start_currency, currency, d, money, v):
    if currency == start_currency and len(v) > 0:
        # print("RETURNING", money < 1.0)
        return money < 1.0

    neighbors = [key[1] for key in d.keys() if key[0] == currency]
    v.add(currency)
    for neighbor in neighbors:
        if neighbor not in v or neighbor == start_currency:
            # print("Checking", currency, "to", neighbor)
            rate = d[(currency, neighbor)]
            if rate < 0:
                rate = 1 / rate
            if arbitrate(start_currency, neighbor, d, money * rate, v):
                return True
    return False

n_currencies = int(input())
while n_currencies > 0:
    currencies = input().split()
    n_conversions = int(input())
    d = {}
    for _ in range(n_conversions):
        a, b, rate = input().split()
        r1, r2 = map(int, rate.split(':'))
        d[(a, b)] = float(r1 / r2)

    arbitrage = False
    for currency in currencies:
        if arbitrate(currency, currency, d, 1.0, set()):
            arbitrage = True
            break

    if arbitrage:
        print("Arbitrage")
    else:
        print("Ok")
    n_currencies = int(input())