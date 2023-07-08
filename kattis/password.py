n = int(input())
nums = sorted([float(input().split()[1]) for _ in range(n)], reverse=True)
print(sum([nums[i] * (i + 1) for i in range(n)]))