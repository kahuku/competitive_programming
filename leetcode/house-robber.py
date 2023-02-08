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

class Solution:
    def rob(self, nums: List[int]) -> int:
        def get_money(i, l):
            if i == 0:
                l[i] = nums[0]
            if i == 1:
                l[i] = max(nums[0], nums[1])
            if l[i] != -1:
                return l[i]
            rob = nums[i] + get_money(i - 2, l)
            skip = get_money(i - 1, l)
            l[i] = max(rob, skip)
            return l[i]
            
        if len(nums) == 1:
            return nums[0]
    
        return get_money(len(nums) - 1, [-1 for _ in range(len(nums))])

class Solution:
    def rob(self, nums: List[int]) -> int:
        self.loot =  [-1 for _ in range(len(nums))]
        def get_money(i):
            if i == 0:
                self.loot[i] = nums[0]
            if i == 1:
                self.loot[i] = max(nums[0], nums[1])
            if self.loot[i] != -1:
                return self.loot[i]
            rob = nums[i] + get_money(i - 2)
            skip = get_money(i - 1)
            self.loot[i] = max(rob, skip)
            return self.loot[i]
            
        if len(nums) == 1:
            return nums[0]
    
        return get_money(len(nums) - 1)
        