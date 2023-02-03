class Solution:
    def rob(self, nums: List[int]) -> int:
        def get_money(nums, i, dp):
            if i == 0:
                dp[0] = nums[0]
            if i == 1:
                dp[1] = max(nums[0], nums[1])
            
            if dp[i] != -1:
                return dp[i]
            
            rob_house = nums[i] + get_money(nums, i - 2, dp)
            skip_house = get_money(nums, i - 1, dp)
            dp[i] = max(rob_house, skip_house)
            return dp[i]

        return get_money(nums, len(nums) - 1, [-1 for i in range(len(nums) + 2)])