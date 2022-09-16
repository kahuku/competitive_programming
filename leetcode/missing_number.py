class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        nums = sorted(nums)
        for i, num in enumerate(nums):
            if num != i:
                return num - 1
        return nums[-1] + 1