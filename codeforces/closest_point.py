# Educational Round 169

for _ in range(int(input())):
    input()
    l = list(map(int, input().split()))
    print("YES" if len(l) == 2 and abs(l[0] - l[-1]) > 1 else "NO")