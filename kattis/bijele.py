nums, set = [int(i) for i in input().split()], [1, 1, 2, 2, 2, 8]
print(' '.join([str(set[i] - nums[i]) for i in range(6)]))