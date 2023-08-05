from collections import defaultdict
d1 = defaultdict(int)
d2 = {}
for _ in range(int(input())):
    name = input()
    d2[name] = input()
for _ in range(int(input())):
    name = input()
    d1[name] += 1
sorted_d1 = sorted(d1.items(), key=lambda x: x[1], reverse=True)
if sorted_d1[0][1] == sorted_d1[1][1]:
    print('tie')
else:
    print(d2[sorted_d1[0][0]])