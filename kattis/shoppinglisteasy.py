n = [int(i) for i in input().split()][0]
s = set(input().split())
for i in range(1, n): s = s.intersection(set(input().split()))
s = sorted(list(s))
print(len(s))
for i in range(len(s)): print(s[i])