class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        dp = [-math.inf]
        for i, num in enumerate(nums):
            dp.append(max(dp[i] + num, num))
        return max(dp)
    
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        dp = nums.copy()
        for i in range(1, len(nums)):
            dp[i] = max(dp[i], dp[i - 1] + dp[i])
        return max(dp)