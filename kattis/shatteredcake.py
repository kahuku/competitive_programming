from functools import reduce
w = int(input())
n = int(input())
area = 0
for i in range(n):
    area += reduce((lambda x, y: x * y), [int(i) for i in input().split()])
print(int(area / w))