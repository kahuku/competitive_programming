class Solution:
    def maximumGap(self, nums: List[int]) -> int:
        nums.sort()
        max_diff = 0
        for i in range(len(nums) - 1):
            if nums[i + 1] - nums[i] > max_diff:
                max_diff = nums[i + 1] - nums[i]
        return max_diff