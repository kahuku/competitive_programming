input()
ma, mi = float('-inf'), float('inf')
for num in list(map(int, input().split())):
    ma = max(ma, num)
    mi = min(mi, num)
print(ma, mi)