#1535A

for _ in range(int(input())):
    a, b, c, d = map(int, input().split())
    print("YES" if all(i in set([max(a, b), max(c, d)]) for i in sorted([a,b,c,d], reverse=True)[:2]) else "NO")