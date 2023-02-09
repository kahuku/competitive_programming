class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums = sorted(list(set(nums)))
        if len(nums) == 1:
            return 1
        run = 1
        longest = 0
        for i in range(1, len(nums)):
            if nums[i] == nums[i - 1] + 1:
                run += 1
            else:
                run = 1
            if run > longest:
                longest = run
        return longest

# ALSO DO UNION FIND SOLUTION