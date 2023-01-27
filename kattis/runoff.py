from sys import stdin
from collections import Counter
names = [line.strip() for line in stdin.readlines()[:-1]]
c = Counter(names)
(name1, count1), (name2, count2) = c.most_common(2)
print(name1 if count1 > count2 else 'Runoff!')