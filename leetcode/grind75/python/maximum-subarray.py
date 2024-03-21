# Dynamic Programming

class Solution:
    # O(n) time | O(n) space
    def maxSubArray(self, nums: List[int]) -> int:
        dp = [float('-inf')] * len(nums)
        dp[0] = nums[0]
        for i in range(1, len(nums)):
            dp[i] = max(0, dp[i - 1]) + nums[i]
        return max(dp)