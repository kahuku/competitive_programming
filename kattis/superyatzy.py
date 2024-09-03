from collections import Counter

n, m = map(int, input().split())
c = Counter([int(input()) for _ in range(n)])
print("Ja" if c.most_common(1)[0][1] + m >= n else "Nej")