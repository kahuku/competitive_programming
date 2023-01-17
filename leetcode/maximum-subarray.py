class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        dp = [-math.inf]
        for i, num in enumerate(nums):
            dp.append(max(dp[i] + num, num))
        return max(dp)