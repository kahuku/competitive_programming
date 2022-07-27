from collections import defaultdict
_ = input()
inp = input()
s = set()
for char in inp:
    if char.lower() not in s:
        s.add(char.lower())
print("YES") if len(s) == 26 else print("NO")