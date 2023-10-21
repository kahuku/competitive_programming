d = {}
n = int(input())
out_order = []
for _ in range(n):
    b = input()
    d[b] = 0
    out_order.append(b)
for _ in range(int(input())):
    for _ in range(n):
        b, vote = input().split()
        if vote == 'yes':
            d[b] += 1
        elif vote == 'no':
            d[b] -= 2
for b in out_order:
    if d[b] == 0:
        print(f"{b} abstain")
    else:
        print(f"{b} {'yes' if d[b] > 0 else 'no'}")