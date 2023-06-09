n = int(input())
s = set()
for _ in range(n):
    s.add(' '.join(input().split('-')).lower())
print(len(s))