#1850A

for _ in range(int(input())):
    l = sorted(list(map(int, input().split())), reverse=True)[:2]
    print("YES" if sum(l) >= 10 else "NO")