from collections import Counter

class Solution:
    def maximizeGreatness(self, nums: List[int]) -> int:
        return len(nums) - max(Counter(nums).values())
    
class Solution:
    def maximizeGreatness(self, nums: List[int]) -> int:
        nums.sort()
        i, j = 0, 0
        ans = 0
        for j in range(len(nums)):
            if nums[j] > nums[i]: 
                ans += 1
                i += 1
        return ans