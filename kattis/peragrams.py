from collections import defaultdict
s = input()
d = defaultdict(int)
for c in s:
    d[c] += 1
odd = len([value for value in list(d.values()) if value % 2 == 1])
print(odd - 1 if odd > 0 else 0)