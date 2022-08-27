nums = sorted([int(i) for i in input().split()], reverse=True)
sum = nums[0]
print(sum - nums[1], sum - nums[2], sum - nums[3])