from collections import Counter
names = input() + input()
letters = input()
if Counter(names) == Counter(letters):
    print("YES")
else:
    print("NO")