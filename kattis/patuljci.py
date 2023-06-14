nums = [int(input()) for _ in range(9)]
s = sum(nums)
for i in range(9):
    for j in range(i + 1, 9):
        if s - nums[i] - nums[j] == 100:
            for k in range(9):
                if k != i and k != j:
                    print(nums[k])
            exit()