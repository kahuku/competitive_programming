size = int(input())
plans = []
for i in range(size):
    nums = list(map(int, input().split()))
    n = 0
    for num in nums:
        n = n | num
    plans.append(n)
print(' '.join(map(str, plans)))