from collections import defaultdict
n, c = map(int, input().split())
d = defaultdict(int)
nums = list(map(int, input().split()))
for num in nums:
    d[num] += 1
l = sorted(d.items(), key=lambda x: (x[1], -nums.index(x[0])), reverse=True)
for i in range(len(l)):
    print((str(l[i][0]) + ' ') * l[i][1], end='')
print()